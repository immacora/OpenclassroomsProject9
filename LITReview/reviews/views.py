from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render, redirect
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
        return super().get_context_data(**kwargs)


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


class ReviewCreateView(LoginRequiredMixin, FormView):
    """Créer une critique qui n'a pas encore de ticket."""
    model = Ticket
    template_name = 'review_new.html'
    login_url = 'login'
    context = {'ticket_form': TicketForm, 'review_form': ReviewForm}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        form = TicketForm(request.POST, request.FILES)
        ticket_title = request.POST['title']
        ticket_description = request.POST['description']
        review_headline = request.POST['headline']
        review_rating = request.POST['rating']
        review_body = request.POST['body']

        try:
            ticket_image = request.FILES['image']
        except MultiValueDictKeyError:
            ticket_image = None

        if form.is_valid():
            new_ticket = Ticket(
                title=ticket_title,
                description=ticket_description,
                image=ticket_image,
                author=self.request.user
            )
            new_review = Review(
                headline=review_headline,
                rating=review_rating,
                body=review_body,
                ticket=new_ticket,
                author=self.request.user
            )
            new_ticket.save()
            new_review.save()
            return redirect('home')
        return render(request, self.template_name, self.context)


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


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    """Modifier une critique."""
    model = Review
    form_class = ReviewForm
    template_name = 'review_edit.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review = Review.objects.get(pk=self.kwargs['pk'])
        ticket_id = review.ticket.id
        ticket = Ticket.objects.get(id=ticket_id)
        context['ticket'] = ticket
        return context


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    """Supprimer une critique."""
    model = Review
    template_name = 'review_delete.html'
    success_url = reverse_lazy('posts')
