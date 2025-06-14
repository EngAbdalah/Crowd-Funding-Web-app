from rest_framework import generics, permissions, status
from allauth.account.utils import complete_signup
from allauth.account import app_settings as allauth_settings
from rest_framework.response import Response
from django.contrib.auth import get_user_model, logout
from rest_framework.views import APIView
from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from .serializers import (
    CustomUserSerializer,
    CustomUserRegisterSerializer,
    PasswordChangeSerializer,
    AccountDeleteSerializer,
)
from rest_framework.exceptions import ValidationError
from allauth.account.models import EmailConfirmation, EmailConfirmationHMAC

User = get_user_model()


class UserDetailAPI(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        # Prevent accidental password updates
        request.data.pop("password", None)
        return super().update(request, *args, **kwargs)


class RegisterAPI(generics.GenericAPIView):
    serializer_class = CustomUserRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()  # Creates inactive user account

        complete_signup(
            request,
            user,
            allauth_settings.EMAIL_VERIFICATION,
            None, 
        )

        return Response(
            {
                "detail": "Verification email sent. Please check your inbox to activate your account.",
                "user": CustomUserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
            },
            status=status.HTTP_201_CREATED,
        )


class ChangePasswordAPI(generics.GenericAPIView):
    serializer_class = PasswordChangeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        # Verify old password
        if not user.check_password(serializer.validated_data["old_password"]):
            return Response(
                {"old_password": ["Incorrect password."]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Set new password
        user.set_password(serializer.validated_data["new_password"])
        user.save()

        return Response(
            {"detail": "Password updated successfully"}, status=status.HTTP_200_OK
        )


class DeleteAccountAPI(generics.GenericAPIView):
    serializer_class = AccountDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        # Verify password
        if not user.check_password(serializer.validated_data["password"]):
            return Response(
                {"password": ["Incorrect password."]},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Logout and delete account
        logout(request)
        user.delete()

        return Response(
            {"detail": "Account deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


class PasswordResetAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        form = PasswordResetForm(request.data)
        if form.is_valid():
            form.save(
                request=request,
                use_https=request.is_secure(),
                from_email=settings.DEFAULT_FROM_EMAIL,
                email_template_name="account/email/password_reset_key_message.txt",
            )
            return Response(
                {"detail": "Password reset email sent"}, status=status.HTTP_200_OK
            )
        return Response(
            {"error": "Password reset failed", "errors": form.errors.as_json()},
            status=status.HTTP_400_BAD_REQUEST,
        )


class CustomConfirmEmailView(APIView):

    # Custom email confirmation view that returns JSON response instead of redirecting to a template.

    def get(self, request, key, *args, **kwargs):
        confirmation = self._get_confirmation_object(key)
        if not confirmation:
            raise ValidationError({"detail": "Invalid or expired confirmation key."})

        confirmation.confirm(request)
        return Response(
            {"detail": "Email confirmed successfully."}, status=status.HTTP_200_OK
        )

    def _get_confirmation_object(self, key):
        # Try HMAC confirmation first (default method used)
        confirmation = EmailConfirmationHMAC.from_key(key)
        if not confirmation:
            # If not HMAC, fall back to DB-stored confirmation (e.g., from older methods)
            try:
                confirmation = EmailConfirmation.objects.get(key=key.lower())
            except EmailConfirmation.DoesNotExist:
                confirmation = None
        return confirmation
