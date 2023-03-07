from django.urls import path
from .views import SignUpView, FollowsPageView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name='signup'),
    path("follows/", FollowsPageView.as_view(), name='follows'),
]