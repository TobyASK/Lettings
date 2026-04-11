"""Align lettings migration state with current model definitions."""

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    """State-only alignment for validators and model options."""

    dependencies = [
        ('lettings', '0001_initial'),
        ('oc_lettings_site', '0002_split_models_to_domain_apps'),
    ]

    operations = [
        # Même principe que la migration 0001 : ajustements d'état uniquement,
        # sans aucune modification SQL (les colonnes existent déjà en base)
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.AlterModelOptions(
                    name='address',
                    options={'verbose_name_plural': 'Addresses'},
                ),
                migrations.AlterModelOptions(
                    name='letting',
                    options={'verbose_name_plural': 'Lettings'},
                ),
                migrations.AlterField(
                    model_name='address',
                    name='country_iso_code',
                    field=models.CharField(
                        max_length=3,
                        validators=[
                            django.core.validators.MinLengthValidator(3)
                        ],
                    ),
                ),
                migrations.AlterField(
                    model_name='address',
                    name='number',
                    field=models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(9999)
                        ],
                    ),
                ),
                migrations.AlterField(
                    model_name='address',
                    name='state',
                    field=models.CharField(
                        max_length=2,
                        validators=[
                            django.core.validators.MinLengthValidator(2)
                        ],
                    ),
                ),
                migrations.AlterField(
                    model_name='address',
                    name='zip_code',
                    field=models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(99999)
                        ],
                    ),
                ),
            ],
            database_operations=[],  # aucun SQL exécuté
        ),
    ]
