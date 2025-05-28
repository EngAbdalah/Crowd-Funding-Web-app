# users/forms.py
from django import forms
from allauth.account.forms import SignupForm
from .models import CustomUser  # Make sure this import is still correct
from phonenumber_field.formfields import PhoneNumberField


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")
    phone = PhoneNumberField(region="EG", label="Phone (Egyptian)")
    birthdate = forms.DateField(
        label="Birthdate", widget=forms.DateInput(attrs={"type": "date"})
    )
    pic = forms.ImageField(required=False, label="Profile Picture")
    country = forms.CharField(max_length=2, label="Country Code (e.g., EG)")

