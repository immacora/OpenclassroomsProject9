from django.urls import path
from .views import FeedsPageView, PostsPageView


urlpatterns = [
    path('', FeedsPageView.as_view(), name='home'),
    path('posts/', PostsPageView.as_view(), name='posts'),
]