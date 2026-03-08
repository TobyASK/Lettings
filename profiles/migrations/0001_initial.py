"""Migrations for profiles app state."""

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """Introduce profile model in migration state without SQL."""

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name='Profile',
                    fields=[
                        (
                            'id',
                            models.AutoField(
                                auto_created=True,
                                primary_key=True,
                                serialize=False,
                                verbose_name='ID',
                            ),
                        ),
                        (
                            'favorite_city',
                            models.CharField(blank=True, max_length=64),
                        ),
                        (
                            'user',
                            models.OneToOneField(
                                on_delete=django.db.models.deletion.CASCADE,
                                to=settings.AUTH_USER_MODEL,
                            ),
                        ),
                    ],
                    options={
                        'db_table': 'oc_lettings_site_profile',
                        'verbose_name_plural': 'Profiles',
                    },
                ),
            ],
            database_operations=[],
        )
    ]
