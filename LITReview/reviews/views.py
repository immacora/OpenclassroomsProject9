from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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


class TicketDetailView(LoginRequiredMixin, DetailView):
    model = Ticket
    context_object_name = 'ticket'
    template_name = 'ticket_detail.html'
    login_url = 'login'


class ReviewDetailView(LoginRequiredMixin, DetailView):
    model = Review
    context_object_name = 'review'
    template_name = 'review_detail.html'
    login_url = 'login'


class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Ticket
    template_name = 'ticket_new.html'
    fields = ('title', 'description', 'image')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'review_new.html'
    fields = ('rating', 'headline', 'body')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.ticket = self.request.ticket
        form.instance.user = self.request.user
        return super().form_valid(form)


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


class TicketDeleteView(LoginRequiredMixin, DeleteView):
    model = Ticket
    template_name = 'ticket_delete.html'
    success_url = reverse_lazy("posts")


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'review_delete.html'
    success_url = reverse_lazy("posts")