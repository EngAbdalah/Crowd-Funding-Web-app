# from django.urls import path
# from . import views
#
# app_name = 'donation'
#
# urlpatterns = [
#     path('donate/<int:project_id>/', views.create_donation, name='create'),
#     path('success/<int:donation_id>/', views.donation_success, name='success'),
#     path('history/', views.donation_history, name='history'),
# ]


from django.urls import path
from . import views

app_name = 'donation'  # This namespace is crucial for URL reversing

urlpatterns = [
    # Donation creation
    path('donate/<int:project_id>/', views.create_donation, name='create'),

    # Success page (requires donation ID)
    path('success/<int:donation_id>/', views.donation_success, name='success'),

    # Donation history
    path('history/', views.donation_history, name='history'),
]