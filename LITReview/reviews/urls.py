from django.urls import path
from .views import (
    FeedsListView,
    PostsListView,
    TicketDetailView,
    TicketUpdateView,
    TicketDeleteView,
    TicketCreateView,
    ReviewCreateView,
    ReviewAddView,
    ReviewDetailView,
    ReviewUpdateView,
    ReviewDeleteView,
    )

urlpatterns = [
    path('', FeedsListView.as_view(), name='home'),
    path('posts/', PostsListView.as_view(), name='posts'),
    path('ticket/new/', TicketCreateView.as_view(), name='ticket_new'),
    path('ticket/<uuid:pk>/', TicketDetailView.as_view(), name='ticket_detail'),
    path('ticket/edit/<uuid:pk>/', TicketUpdateView.as_view(), name='ticket_edit'),
    path('ticket/delete/<uuid:pk>/', TicketDeleteView.as_view(), name='ticket_delete'),
    path('review/new/', ReviewCreateView.as_view(), name='review_new'),
    path('review/add/<uuid:pk>', ReviewAddView.as_view(), name='review_add'),
    path('review/<uuid:pk>/', ReviewDetailView.as_view(), name='review_detail'),
    path('review/edit/<uuid:pk>/', ReviewUpdateView.as_view(), name='review_edit'),
    path('review/delete/<uuid:pk>/', ReviewDeleteView.as_view(), name='review_delete'),
]