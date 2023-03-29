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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['username'].label = ""
        self.fields['password1'].label = ""
        self.fields['password2'].label = ""
        self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-register', 'placeholder': "Nom d'utilisateur"})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-register', 'placeholder': "Mot de passe"})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-register', 'placeholder': "Confirmer le mot de passe"})


class CustomUserChangeForm(UserChangeForm):
    """Formulaire de modification de compte CustomUser."""

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ['username',]


class UserFollowerManagementForm(forms.Form):
    """Formulaire de gestion des d'abonnements à un compte utilisateur."""
    add_follower = forms.CharField(
        max_length=191,
        required=False,
        label='',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['add_follower'].widget = forms.TextInput(attrs={'class': 'form-add_follower', 'placeholder': "Nom d'utilisateur"})
