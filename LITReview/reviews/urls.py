from django.urls import path
from .views import (
    FeedsListView,
    PostsListView,
    TicketDetailView,
    ReviewDetailView,
    TicketUpdateView,
    ReviewUpdateView,
    TicketDeleteView,
    ReviewDeleteView,
    TicketCreateView,
    ReviewCreateView,
    )


urlpatterns = [
    #path('posts/<uuid:pk>/', ReviewDetailView.as_view(), name='review_detail'),
    path('posts/<uuid:pk>/', TicketDetailView.as_view(), name='ticket_detail'),
    path('posts/<uuid:pk>/edit/', TicketUpdateView.as_view(), name='ticket_edit'),
    #path('posts/<uuid:pk>/edit/', ReviewUpdateView.as_view(), name='review_edit'),
    path('posts/<uuid:pk>/delete/', TicketDeleteView.as_view(), name='ticket_delete'),
    #path('posts/<uuid:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
    path('ticket/new/', TicketCreateView.as_view(), name='ticket_new'),
    path('review/new/', ReviewCreateView.as_view(), name='review_new'),
    path('posts/', PostsListView.as_view(), name='posts'),
    path('', FeedsListView.as_view(), name='home'),
]