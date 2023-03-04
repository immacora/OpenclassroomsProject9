from django.urls import path
from . import views


urlpatterns = [
    path("home/", views.feeds, name="home"),
]