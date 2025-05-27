from django.urls import path
from . import views

app_name = 'donation'

urlpatterns = [
    path('donate/<int:project_id>/', views.create_donation, name='donate'),
]