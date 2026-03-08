"""Remove legacy model state from core app after modular split."""

from django.db import migrations


class Migration(migrations.Migration):
    """State-only cleanup of legacy models from project app."""

    dependencies = [
        ('lettings', '0001_initial'),
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.RemoveField(
                    model_name='letting',
                    name='address',
                ),
                migrations.RemoveField(
                    model_name='profile',
                    name='user',
                ),
                migrations.DeleteModel(name='Address'),
                migrations.DeleteModel(name='Letting'),
                migrations.DeleteModel(name='Profile'),
            ],
            database_operations=[],
        ),
    ]
