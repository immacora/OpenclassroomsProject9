"""LITReview URL Configuration"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # User management
    path('users/', include('django.contrib.auth.urls')),

    # Local apps
    path('users/', include('users.urls')),
    path('', include("reviews.urls")),  
]
