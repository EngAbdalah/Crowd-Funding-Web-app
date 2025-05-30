from django.urls import path
from .views import (
    comment_list, comment_detail,
    reply_list, reply_detail,
    rate_list, rate_detail
)

urlpatterns = [
    path('comments/', comment_list),
    path('comments/<int:pk>/', comment_detail),
    path('replies/', reply_list),
    path('replies/<int:pk>/', reply_detail),
    path('rates/', rate_list),
    path('rates/<int:pk>/', rate_detail),
]