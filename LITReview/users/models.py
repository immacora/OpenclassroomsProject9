from django.conf import settings
from django.contrib.auth.models import AbstractUser
import uuid
from django.db import models


class CustomUser(AbstractUser):
    """Utilisateur personnalisé."""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    followed_user = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='UserFollower'
    )

    def __str__(self):
        return self.username


class UserFollower(models.Model):
    """Abonné."""
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='userfollower_user'
    )
    followed_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='userfollower_followed_user'
    )

    class Meta:
        unique_together=('user', 'followed_user')

    def __str__(self):
        return f"{self.user.username} suit {self.followed_user.username}"
