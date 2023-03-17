from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
import uuid
from django.db import models
from django.urls import reverse


class Ticket(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(
        'Titre ',
        max_length = 128
    )
    description = models.TextField(
        max_length = 2048,
        blank = True
    )
    image = models.ImageField(
        upload_to = 'images/',
        null = True,
        blank = True
    )
    user = models.ForeignKey(
        to = settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        verbose_name = 'utilisateur',
    )
    time_created = models.DateTimeField(
        'Date de création',
        auto_now_add = True
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('ticket_detail', args=[str(self.id)])
    
    #class Meta:
        #ordering = ["-time_created"]


class Review(models.Model):
    RATING_NUMBER = (
        (1, '-1'),
        (2, '-2'),
        (3, '-3'),
        (4, '-4'),
        (5, '-5'),
    )
    ticket = models.ForeignKey(
        to = Ticket,
        on_delete = models.CASCADE,
        related_name='review_ticket',
    )
    rating = models.PositiveSmallIntegerField(
        'Note ',
        validators = [MinValueValidator(0), MaxValueValidator(5)],
        choices = RATING_NUMBER
    )
    headline = models.CharField(
        'Titre ',
        max_length = 128
    )
    body = models.TextField(
        'Commentaire',
        max_length = 8192,
        blank = True
    )
    user = models.ForeignKey(
        to = settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        verbose_name = 'utilisateur',
    )
    time_created = models.DateTimeField(
        'Date de création',
        auto_now_add = True
    )

    def __str__(self):
        return f"Critique du ticket : {self.ticket}"
    
    def get_absolute_url(self):
        return reverse('ticket_detail', args=[str(self.id)])

