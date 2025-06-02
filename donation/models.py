from django.db import models
from django.contrib.auth.models import User

class Donation(models.Model):
    PROJECT_CHOICES = [
        ('project1', 'Project 1'),
        ('project2', 'Project 2'),
        ('project3', 'Project 3'),
    ]
    CURRENCY_CHOICES = [('USD','USD'), ('EUR','EUR'),('EG','EG')]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    project = models.CharField(max_length=20, choices=PROJECT_CHOICES)
    date = models.DateField(auto_now_add=True)
    currency = models.CharField(max_length=10,choices=CURRENCY_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} donated {self.amount} {self.currency} to {self.project}"
