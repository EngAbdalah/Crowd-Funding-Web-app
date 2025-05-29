from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from users.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    desc = models.TextField()

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Project(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    details = models.TextField()
    total_target = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(1000)]  # Min 1000 EGP
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    is_cancelled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.start_date and self.end_date:
            if self.start_date >= self.end_date:
                raise ValidationError("End date must be after start date")
            if self.end_date <= timezone.now():
                raise ValidationError("End date must be in the future")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    @property
    def current_funding(self):
        return self.donate_set.aggregate(sum=models.Sum('amount'))['sum'] or 0

    @property
    def funding_percentage(self):
        return (self.current_funding / self.total_target) * 100

    @property
    def average_rating(self):
        avg = self.ratings.aggregate(avg=models.Avg('stars'))['avg']
        return round(avg, 1) if avg else 0

    class Meta:
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['category']),
            models.Index(fields=['status']),
            models.Index(fields=['created_at']),
            models.Index(fields=['start_date']),
            models.Index(fields=['end_date']),
            models.Index(fields=['is_cancelled']),
            models.Index(fields=['status', 'created_at']),
            models.Index(fields=['user', 'status']),
            models.Index(fields=['category', 'status']),
        ]

    def __str__(self):
        return self.title

class ProjectTag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tags')
    tagname = models.CharField(max_length=30)

    class Meta:
        indexes = [
            models.Index(fields=['project']),
            models.Index(fields=['tagname']),
            models.Index(fields=['project', 'tagname']),
        ]
        unique_together = ['project', 'tagname']

    def __str__(self):
        return self.tagname

class ProjectPic(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='pictures')
    pic = models.ImageField(upload_to='projects/')

    class Meta:
        indexes = [
            models.Index(fields=['project']),
        ]

    def __str__(self):
        return f"Picture for {self.project.title}"