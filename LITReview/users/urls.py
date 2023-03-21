from django.urls import path
from .views import SignUpView, FollowsPageView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<uuid:pk>/follows/', FollowsPageView.as_view(), name='follows'),
]