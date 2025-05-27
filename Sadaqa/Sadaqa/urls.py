# from django.contrib import admin
# from django.urls import path, include
# from django.contrib.auth import views as auth_views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('donations/', include('donation.urls')),
#     path('projects/', include('projects.urls')),
#     path('users/', include('users.urls')),
#     path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
#     path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
# ]



# from django.contrib import admin
# from django.urls import path, include
# from django.contrib.auth import views as auth_views
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('accounts/', include([
#         path('login/', auth_views.LoginView.as_view(), name='login'),
#         path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#         path('register/', include('users.urls')),
#     ])),
#     path('donations/', include('donation.urls')),
#     path('projects/', include('projects.urls')),
# ]

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include([
        path('login/', auth_views.LoginView.as_view(), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('register/', include('users.urls')),  # This is correct
    ])),
    path('donations/', include('donation.urls')),
    path('projects/', include('projects.urls')),
]