from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class PostsPageView(TemplateView):
    template_name = "posts.html"
