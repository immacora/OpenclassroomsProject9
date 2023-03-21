from django.urls import path
from .views import (
    FeedsListView,
    PostsListView,
    TicketDetailView,
    TicketUpdateView,
    TicketDeleteView,
    TicketCreateView,
    )

urlpatterns = [
    path('', FeedsListView.as_view(), name='home'),
    path('posts/', PostsListView.as_view(), name='posts'),
    path('ticket/new/', TicketCreateView.as_view(), name='ticket_new'),
    path('<uuid:pk>/', TicketDetailView.as_view(), name='ticket_detail'),
    path('<uuid:pk>/edit/', TicketUpdateView.as_view(), name='ticket_edit'),
    path('<uuid:pk>/delete/', TicketDeleteView.as_view(), name='ticket_delete'),
]