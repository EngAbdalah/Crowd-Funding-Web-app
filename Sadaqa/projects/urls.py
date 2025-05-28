from django.urls import path
from .views import ProjectDetailView, ProjectCreateView

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='project_create'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
]