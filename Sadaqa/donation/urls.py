from django.urls import path
from . import views

app_name = 'donation'

urlpatterns = [
    path('donate/<int:project_id>/', views.create_donation, name='create'),
    path('success/<int:donation_id>/', views.donation_success, name='success'),
    path('history/', views.donation_history, name='history'),
    path('receipt/<int:pk>/', views.donation_receipt, name='receipt'),
]