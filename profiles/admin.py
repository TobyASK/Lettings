"""Admin configuration for profiles app."""

from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Admin display for profiles."""

    list_display = ('user', 'favorite_city')
