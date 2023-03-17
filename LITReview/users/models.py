from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid
from django.db import models


class CustomUser(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    def __str__(self):
        return self.username


class UserFollows(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='utilisateur',
    )
    followed_user = models.ForeignKey(
        to = settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name='followed_by',
        verbose_name = 'utilisateur suivi',
    )
    time_created = models.DateTimeField(
        'Date de création',
        auto_now_add = True
    )

    class Meta:
        unique_together = ('user', 'followed_user', )

    def __str__(self):
        return self.user
