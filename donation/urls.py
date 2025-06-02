from django.urls import path
from . import views

urlpatterns = [
    path('', views.donate, name='donate'),
    path('success/<int:donation_id>/', views.success, name='success'),
    path('history/', views.history, name='history'),
]