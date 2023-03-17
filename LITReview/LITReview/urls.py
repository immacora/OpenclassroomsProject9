"""LITReview URL Configuration"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # User management
    path('users/', include('django.contrib.auth.urls')),

    # Local apps
    path('users/', include('users.urls')),
    path('', include('reviews.urls')),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
