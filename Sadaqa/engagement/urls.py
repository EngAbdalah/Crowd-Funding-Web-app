from django.urls import path
from .views import *

urlpatterns = [
    path('comments/', comment_list),
    path('comments/<int:pk>/', comment_detail),
    path('replies/', reply_list),
    path('replies/<int:pk>/', reply_detail),
    path('rates/', rate_list),
    path('rates/<int:pk>/', rate_detail),
    path('projects/<int:project_id>/comments/create/', create_comment, name='create-comment'),
    path('comments/<int:comment_id>/replies/create/', create_reply, name='create-reply'),
]