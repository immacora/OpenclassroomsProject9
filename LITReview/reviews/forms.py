from django import forms

from .models import Ticket, Review


class TicketForm(forms.ModelForm):
    """Formulaire de création de ticket."""

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image',]


class ReviewForm(forms.ModelForm):
    """Formulaire de création de critique."""

    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body',]
        widgets = {'rating': forms.RadioSelect()}