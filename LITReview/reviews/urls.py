from django.urls import path
from .views import FeedsListView, PostsListView, TicketDetailView ,ReviewDetailView


urlpatterns = [
    path('', FeedsListView.as_view(), name='home'),
    path('posts/', PostsListView.as_view(), name='posts'),
    path('posts/<uuid:pk>/', TicketDetailView.as_view(), name='ticket_detail'),
    path('posts/<uuid:pk>/', ReviewDetailView.as_view(), name='review_detail'),
]