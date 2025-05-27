from django.db import models

# Create your models here.


# .........created by Jalal.................. to test donation app



from django.db import models
from users.models import CustomUser

class Project(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    total_target = models.DecimalField(max_digits=12, decimal_places=2)
    current_donations = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_projects')

    def __str__(self):
        return self.title