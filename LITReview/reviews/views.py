from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView


class HomePageView(TemplateView):
    template_name = 'home.html'


class PostsPageView(TemplateView):
    template_name = 'posts.html'
