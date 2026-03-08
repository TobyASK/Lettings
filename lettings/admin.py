"""Admin configuration for lettings app."""

from django.contrib import admin

from .models import Address, Letting


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    """Admin display for addresses."""

    list_display = (
        'number',
        'street',
        'city',
        'state',
        'zip_code',
        'country_iso_code',
    )


@admin.register(Letting)
class LettingAdmin(admin.ModelAdmin):
    """Admin display for lettings."""

    list_display = ('title', 'address')
