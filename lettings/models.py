"""Data models for lettings domain."""

from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


class Address(models.Model):
    """Postal address for a letting."""

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999)]
    )
    country_iso_code = models.CharField(
        max_length=3,
        validators=[MinLengthValidator(3)],
    )

    class Meta:
        """Metadata for Address model."""

        verbose_name_plural = 'Addresses'

    def __str__(self):
        """Return display value for admin and templates."""
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """Rental listing entity."""

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        """Metadata for Letting model."""

        verbose_name_plural = 'Lettings'

    def __str__(self):
        """Return display value for admin and templates."""
        return self.title
