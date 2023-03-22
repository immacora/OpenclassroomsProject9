from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from .models import Ticket, Review
from .forms import TicketForm, ReviewForm


class FeedsListView(LoginRequiredMixin, ListView):
    """Afficher la liste des tickets des utilisateurs suivis par l'utilisateur connecté avec leur critique."""
    context_object_name = 'ticket_list'
    queryset = Ticket.objects.all()
    template_name = 'home.html'
    login_url = 'login'


class PostsListView(LoginRequiredMixin, ListView):
    """Afficher la liste des tickets et critiques de l'utilisateur connecté."""
    model = Ticket
    context_object_name = 'ticket_list'
    template_name = 'posts.html'
    login_url = 'login'


class TicketCreateView(LoginRequiredMixin, CreateView):
    """Créer un ticket."""
    model = Ticket
    form_class = TicketForm
    template_name = 'ticket_new.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TicketDetailView(LoginRequiredMixin, DetailView):
    """Afficher le détail d'un ticket."""
    model = Ticket
    context_object_name = 'ticket'
    template_name = 'ticket_detail.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TicketUpdateView(LoginRequiredMixin, UpdateView):
    """Modifier un ticket."""
    model = Ticket
    form_class = TicketForm
    template_name = 'ticket_edit.html'
    login_url = 'login'


class TicketDeleteView(LoginRequiredMixin, DeleteView):
    """Supprimer un ticket."""
    model = Ticket
    template_name = 'ticket_delete.html'
    success_url = reverse_lazy('posts')


class ReviewAddView(LoginRequiredMixin, FormView):
    """Ajouter une critique à un ticket déjà créé."""
    form_class = ReviewForm
    template_name = 'review_add.html'
    login_url = 'login'

    def get(self, request, pk):
        form = self.form_class()
        ticket = Ticket.objects.get(id=pk)
        context = {
            'form': form,
            'ticket': ticket,
        }
        return render(request, self.template_name, context)
    
    def post(self, request, pk):
        form = self.form_class(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.ticket = Ticket.objects.get(id=pk)
            form.instance.author = self.request.user
            review.save()
            return redirect('home')
        return render(request, self.template_name, context={'form': form})


class ReviewDetailView(LoginRequiredMixin, DetailView):
    """Afficher le détail d'une critique avec son ticket."""
    template_name = 'review_detail.html'
    login_url = 'login'

    def get(self, request, pk):
        review = Review.objects.get(id=pk)
        ticket_id = review.ticket.id
        ticket = Ticket.objects.get(id=ticket_id)
        context = {
            'review': review,
            'ticket': ticket,
        }
        return render(request, self.template_name, context)


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    """Supprimer une critique."""
    model = Review
    template_name = 'review_delete.html'
    success_url = reverse_lazy('posts')