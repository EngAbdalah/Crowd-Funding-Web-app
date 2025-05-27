from django.db import models
from users.models import CustomUser  # Assuming this is your user model
from projects.models import Project  # From projects app


class Donation(models.Model):
    CURRENCY_CHOICES = [
        ('EGP', 'Egyptian Pound'),
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
    ]

    donor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='donations')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='donations')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='EGP')
    donation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-donation_date']

    def __str__(self):
        return f"{self.donor.email} donated {self.amount} {self.currency} to {self.project.title}"