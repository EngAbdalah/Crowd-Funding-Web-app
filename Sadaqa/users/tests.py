from django.test import TestCase, Client
from django.urls import reverse
from users.models import CustomUser
from datetime import date


class LoginTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse("account_login")

        # Create user with ALL required fields
        self.user = CustomUser.objects.create_user(
            username="testuser",  # Required
            email="test@example.com",
            password="testpass123",
            phone="+201234567890",  # Example Egyptian number
            birthdate=date(2000, 1, 1),
            country="EG",
        )

    def test_login_page_loads(self):
        response = self.client.get(self.login_url)
        self.assertTemplateUsed(response, "account/login.html")

    def test_valid_login(self):
        response = self.client.post(
            self.login_url,
            {
                "login": "testuser",  # Login with username or email
                "password": "testpass123",
            },
        )
        self.assertRedirects(response, "/")  # Update to your success URL


class SignupTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse("account_signup")

    def test_signup_page_loads(self):
        response = self.client.get(self.signup_url)
        self.assertTemplateUsed(response, "account/signup.html")

    def test_valid_signup(self):
        data = {
            "username": "newuser",
            "email": "new@example.com",
            "password1": "StrongPass123!",
            "password2": "StrongPass123!",
            "phone": "+201234567890",  # Required
            "birthdate": "2000-01-01",  # Format: YYYY-MM-DD
            "country": "EG",
        }
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, 302)  # Now redirects
