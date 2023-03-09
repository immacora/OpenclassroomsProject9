from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView
from .models import Ticket, Review


class HomePageView(LoginRequiredMixin, ListView):
    template_name = 'home.html'
    model = Ticket
    login_url = 'login'


class PostsPageView(LoginRequiredMixin, TemplateView):
    template_name = 'posts.html'
    login_url = 'login'
