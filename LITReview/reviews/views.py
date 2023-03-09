from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView
from .models import Ticket, Review


class FeedsPageView(LoginRequiredMixin, ListView):
    model = Ticket
    context_object_name = 'ticket_list'
    template_name = 'home.html'
    login_url = 'login'


class PostsPageView(LoginRequiredMixin, TemplateView):
    template_name = 'posts.html'
    login_url = 'login'
