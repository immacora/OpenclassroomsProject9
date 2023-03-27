from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from crispy_forms.helper import FormHelper

CustomUser = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    """Formulaire de création de compte CustomUser."""

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username',]


class CustomUserChangeForm(UserChangeForm):
    """Formulaire de modification de compte CustomUser."""

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ['username',]


class AddUserFollowerForm(forms.Form):
    """Formulaire d'ajout d'abonnement à un compte utilisateur."""
    add_follower = forms.CharField(
        max_length=191,
        required=False,
        label='',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['add_follower'].widget.attrs['placeholder'] = "Nom d'utilisateur"
