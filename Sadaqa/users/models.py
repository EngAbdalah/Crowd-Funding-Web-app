from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import (
    PhoneNumberField,
)  #need pip install django-phonenumber-field
from django_countries.fields import (
    CountryField,
)  # need pip install django-countries


# Create your models here.
class CustomUser(AbstractUser):
    # fields inherited from AbstractUser by defualt are
    # email
    # username
    # password
    # first_name
    # last_name
    phone = PhoneNumberField(unique=True)
    birthdate = models.DateField(null=False)
    pic = models.ImageField(upload_to="profile_pics/", null=True, blank=True)
    country = CountryField(default="EG")

    def __str__(self):
        return self.username
