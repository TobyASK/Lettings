"""Move lettings models state from core app to dedicated app."""

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    """State-only migration to attach existing tables to lettings app."""

    initial = True

    dependencies = [
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name='Address',
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
                        ('number', models.PositiveIntegerField()),
                        ('street', models.CharField(max_length=64)),
                        ('city', models.CharField(max_length=64)),
                        ('state', models.CharField(max_length=2)),
                        ('zip_code', models.PositiveIntegerField()),
                        ('country_iso_code', models.CharField(max_length=3)),
                    ],
                    options={
                        'db_table': 'oc_lettings_site_address',
                    },
                ),
                migrations.CreateModel(
                    name='Letting',
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
                        ('title', models.CharField(max_length=256)),
                        (
                            'address',
                            models.OneToOneField(
                                on_delete=django.db.models.deletion.CASCADE,
                                to='lettings.address',
                            ),
                        ),
                    ],
                    options={
                        'db_table': 'oc_lettings_site_letting',
                    },
                ),
            ],
            database_operations=[],
        ),
    ]
