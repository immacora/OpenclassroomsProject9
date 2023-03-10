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
    title = models.CharField(max_length = 128)
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
        on_delete = models.CASCADE
    )
    time_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('ticket_detail', args=[str(self.id)])


class Review(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    ticket = models.ForeignKey(
        to = Ticket,
        on_delete = models.CASCADE,
        related_name='reviews',
    )
    rating = models.PositiveSmallIntegerField(
        max_length = 1024,
        validators = [MinValueValidator(0), MaxValueValidator(5)]
    )
    headline = models.CharField(max_length = 128)
    body = models.TextField(
        max_length = 8192,
        blank = True
    )
    user = models.ForeignKey(
        to = settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
    )
    time_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Critique du ticket : {self.ticket}"
    
    def get_absolute_url(self):
        return reverse('review_detail', args=[str(self.id)])
