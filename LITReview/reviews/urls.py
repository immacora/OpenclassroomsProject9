from django.urls import path
from .views import HomePageView, PostsPageView


urlpatterns = [
    path("home/", HomePageView.as_view(), name="home"),
    path("posts/", PostsPageView.as_view(), name="posts"),
]