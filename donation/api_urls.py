from django.urls import path
from . import api_views

urlpatterns = [
    path('donations/', api_views.DonationListCreate.as_view(), name='donation-list-create'),
    path('donations/<int:pk>/', api_views.DonationRetrieveUpdateDestroy.as_view(), name='donation-detail'),
]
