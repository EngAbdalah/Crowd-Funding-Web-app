from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    # Template-based authentication views
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html", redirect_authenticated_user=True
        ),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),

    # =============================================
    # USER API AUTHENTICATION ENDPOINTS
    # =============================================
    path('api/auth/register/', views.user_register, name='user-register'),
    path('api/auth/login/', views.user_login, name='user-login'),
    path('api/auth/logout/', views.user_logout, name='user-logout'),

    # =============================================
    # USER API CRUD ENDPOINTS
    # =============================================
    path('api/users/', views.user_list, name='user-list'),
    path('api/users/profile/', views.user_profile, name='user-profile'),
    path('api/users/profile/update/', views.user_update, name='user-profile-update'),
    path('api/users/change-password/', views.user_change_password, name='user-change-password'),
    path('api/users/delete/', views.user_delete, name='user-delete'),
    path('api/users/<int:pk>/', views.user_detail, name='user-detail'),
    path('api/users/<int:pk>/update/', views.user_update, name='user-update'),
    path('api/users/<int:pk>/delete/', views.user_delete, name='user-delete-admin'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static to allow input image to be saved in the media folder in development phase only
