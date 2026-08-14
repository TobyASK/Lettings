"""Data models for profiles domain."""

from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """User profile model."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        """Metadata for Profile model."""

        verbose_name_plural = 'Profiles'

    def __str__(self):
        """Return display value for admin and templates."""
        return self.user.username
