# users/adapter.py
from allauth.account.adapter import DefaultAccountAdapter
from .forms import CustomSignupForm


class CustomAccountAdapter(DefaultAccountAdapter):

    def get_signup_form_class(self, request):
        """
        Returns the form class to use for the signup form.
        This tells Allauth to use your CustomSignupForm.
        """
        return CustomSignupForm

    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form. This is where you connect your custom fields.
        """
        # Call the super method first. Pass commit=False to prevent
        # an early save by Allauth before your custom fields are set.
        user = super().save_user(request, user, form, False)

        # Now, assign your custom fields from the form's cleaned_data
        # Use .get() for fields that might be optional (though here they're all required)
        user.first_name = form.cleaned_data.get("first_name")
        user.last_name = form.cleaned_data.get("last_name")
        user.phone = form.cleaned_data.get("phone")
        user.birthdate = form.cleaned_data.get("birthdate")
        user.pic = form.cleaned_data.get("pic")
        user.country = form.cleaned_data.get("country")

        # Only save the user object to the database if commit is True
        if commit:
            user.save()
        return user
