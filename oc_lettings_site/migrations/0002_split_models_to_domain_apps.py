"""Copy legacy data to new apps then remove legacy core tables."""

from django.db import migrations


def copy_legacy_to_new_apps(apps, schema_editor):
    """Create empty new tables and transfer legacy data into them."""
    db_alias = schema_editor.connection.alias

    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')

    NewAddress = apps.get_model('lettings', 'Address')
    NewLetting = apps.get_model('lettings', 'Letting')
    NewProfile = apps.get_model('profiles', 'Profile')

    NewAddress.objects.using(db_alias).bulk_create(
        [
            NewAddress(
                id=address.id,
                number=address.number,
                street=address.street,
                city=address.city,
                state=address.state,
                zip_code=address.zip_code,
                country_iso_code=address.country_iso_code,
            )
            for address in OldAddress.objects.using(db_alias).all()
        ],
        ignore_conflicts=True,
    )

    NewLetting.objects.using(db_alias).bulk_create(
        [
            NewLetting(
                id=letting.id,
                title=letting.title,
                address_id=letting.address_id,
            )
            for letting in OldLetting.objects.using(db_alias).all()
        ],
        ignore_conflicts=True,
    )

    NewProfile.objects.using(db_alias).bulk_create(
        [
            NewProfile(
                id=profile.id,
                user_id=profile.user_id,
                favorite_city=profile.favorite_city,
            )
            for profile in OldProfile.objects.using(db_alias).all()
        ],
        ignore_conflicts=True,
    )


def copy_new_apps_to_legacy(apps, schema_editor):
    """Reverse transfer for migration rollback."""
    db_alias = schema_editor.connection.alias

    OldAddress = apps.get_model('oc_lettings_site', 'Address')
    OldLetting = apps.get_model('oc_lettings_site', 'Letting')
    OldProfile = apps.get_model('oc_lettings_site', 'Profile')

    NewAddress = apps.get_model('lettings', 'Address')
    NewLetting = apps.get_model('lettings', 'Letting')
    NewProfile = apps.get_model('profiles', 'Profile')

    OldAddress.objects.using(db_alias).bulk_create(
        [
            OldAddress(
                id=address.id,
                number=address.number,
                street=address.street,
                city=address.city,
                state=address.state,
                zip_code=address.zip_code,
                country_iso_code=address.country_iso_code,
            )
            for address in NewAddress.objects.using(db_alias).all()
        ],
        ignore_conflicts=True,
    )

    OldLetting.objects.using(db_alias).bulk_create(
        [
            OldLetting(
                id=letting.id,
                title=letting.title,
                address_id=letting.address_id,
            )
            for letting in NewLetting.objects.using(db_alias).all()
        ],
        ignore_conflicts=True,
    )

    OldProfile.objects.using(db_alias).bulk_create(
        [
            OldProfile(
                id=profile.id,
                user_id=profile.user_id,
                favorite_city=profile.favorite_city,
            )
            for profile in NewProfile.objects.using(db_alias).all()
        ],
        ignore_conflicts=True,
    )


class Migration(migrations.Migration):
    """Migrate legacy data and remove legacy core models."""

    dependencies = [
        ('lettings', '0001_initial'),
        ('profiles', '0001_initial'),
        ('oc_lettings_site', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            code=copy_legacy_to_new_apps,
            reverse_code=copy_new_apps_to_legacy,
        ),
        migrations.DeleteModel(name='Letting'),
        migrations.DeleteModel(name='Address'),
        migrations.DeleteModel(name='Profile'),
    ]
