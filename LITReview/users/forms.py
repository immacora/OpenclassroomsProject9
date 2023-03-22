from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    """Formulaire de création de compte CustomUser."""

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username',)


class CustomUserChangeForm(UserChangeForm):
    """Formulaire de modification de compte CustomUser."""

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('username',)
