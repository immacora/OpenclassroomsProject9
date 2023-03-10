from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import Ticket, Review


class FeedsListView(LoginRequiredMixin, ListView):
    model = Ticket
    context_object_name = 'ticket_list'
    template_name = 'home.html'
    login_url = 'login'


class PostsListView(LoginRequiredMixin, ListView):
    model = Ticket
    context_object_name = 'ticket_list'
    template_name = 'posts.html'
    login_url = 'login'


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    template_name = 'ticket_new.html'
    fields = ["title", "description", "image"]
    login_url = 'login'


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'review_new.html'
    fields = ["ticket", "rating", "headline", "body"]
    login_url = 'login'


class TicketUpdateView(LoginRequiredMixin, UpdateView):
    model = Ticket
    template_name = 'ticket_edit.html'
    fields = ["title", "description", "image"]
    login_url = 'login'


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    template_name = 'review_edit.html'
    fields = ["rating", "headline", "body"]
    login_url = 'login'
