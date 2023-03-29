from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.db import IntegrityError
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView

from .models import UserFollower
from .forms import CustomUserCreationForm, UserFollowerManagementForm

CustomUser = get_user_model()


class SignUpView(CreateView):
    """Créer un compte CustomUser."""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"


class FollowsPageView(LoginRequiredMixin, FormView):
    """
    Afficher les abonnements/abonnés de l'utilisateur connecté et lui permettre d'en suivre ou arrêter d'en suivre.

    Affiche les abonnements et les abonnés de l'utilisateur connecté.
    Si l'un des deux boutons du template envoie une donnée,
    vérifie le nom d'utilisateur saisi dans l'input et crée l'abonné dans la table pivot,
    ou supprime l'abonné.
    """
    template_name = 'follows.html'
    form_class = UserFollowerManagementForm
    message = ''
    login_url = 'login'

    def get(self, request, pk):
        form = self.form_class()
        subscriptions = UserFollower.objects.filter(user=pk)
        subscribers = UserFollower.objects.filter(followed_user=pk)
        context = {
            'form': form,
            'subscriptions': subscriptions,
            'subscribers': subscribers,
        }
        return render(request, self.template_name, context)
    
    def post(self, request, pk):
        form = self.form_class(request.POST)

        if form.is_valid():
            try:
                if request.POST['add_follower']:
                    try:
                        user_to_follow = CustomUser.objects.get(username=request.POST['add_follower'])
                        if user_to_follow == request.user:
                            messages.error(request, "Vous ne pouvez vous abonner à votre propre compte.")
                        else:
                            try:
                                UserFollower.objects.create(user=request.user, followed_user=user_to_follow)
                            except IntegrityError:
                                messages.error(request, "L'utilisateur saisi se trouve déjà dans la liste de vos abonnements.")
                    except CustomUser.DoesNotExist:
                        messages.error(request, "L'utilisateur saisi n'existe pas.")

                elif request.POST['unfollow']:
                    user_to_unfollow_id = request.POST['unfollow']
                    user_to_unfollow = UserFollower.objects.get(id=user_to_unfollow_id)
                    user_to_unfollow.delete()

            except MultiValueDictKeyError:
                messages.error(request, "Vous n'avez pas saisi de nom d'utilisateur.")

            return redirect('follows', pk)

        return render(request, self.template_name, context={'form': form})
