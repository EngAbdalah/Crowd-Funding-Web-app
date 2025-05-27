# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from phonenumber_field.modelfields import (
#     PhoneNumberField,
# )  #need pip install django-phonenumber-field
# from django_countries.fields import (
#     CountryField,
# )  # need pip install django-countries
#
#
# # Create your models here.
# class CustomUser(AbstractUser):
#     # fields inherited from AbstractUser by defualt are
#     # email
#     # username
#     # password
#     # first_name
#     # last_name
#
#     phone = PhoneNumberField(unique=True,region="EG")
#     birthdate = models.DateField()
#     pic = models.ImageField(upload_to="profile_pics/", null=True, blank=True)
#     country = CountryField(default="EG")
#
#     def __str__(self):
#         return self.username

# .........Jalal Commeted the above code to run this app, as it is related to donation app,
# so I need to run it intially- just to test my app donation

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.email