from django.urls import path
from .views import (
    FeedsListView,
    PostsListView,
    TicketCreateView,
    ReviewCreateView,
    TicketUpdateView,
    ReviewUpdateView
    )


urlpatterns = [
    path('review/new/', ReviewCreateView.as_view(), name='review_new'),
    path('ticket/new/', TicketCreateView.as_view(), name='ticket_new'),
    path('posts/<uuid:pk>/edit/', TicketUpdateView.as_view(), name='ticket_edit'),
    path('posts/', PostsListView.as_view(), name='posts'),
    path('', FeedsListView.as_view(), name='home'),
]