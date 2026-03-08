"""Tests for lettings app."""

import pytest
from django.urls import reverse

from lettings.models import Address, Letting


@pytest.fixture
def address(db):
    """Create an address fixture."""
    return Address.objects.create(
        number=10,
        street='Main St',
        city='Denver',
        state='CO',
        zip_code=80203,
        country_iso_code='USA',
    )


@pytest.fixture
def letting(db, address):
    """Create a letting fixture."""
    return Letting.objects.create(title='Test letting', address=address)


@pytest.mark.django_db
def test_lettings_index_returns_200(client, letting):
    """The lettings list page should return HTTP 200."""
    response = client.get(reverse('lettings_index'))
    assert response.status_code == 200
    assert 'Test letting' in response.content.decode()


@pytest.mark.django_db
def test_letting_detail_returns_200(client, letting):
    """The letting details page should return HTTP 200."""
    response = client.get(
        reverse('letting', kwargs={'letting_id': letting.id})
    )
    assert response.status_code == 200
    assert 'Main St' in response.content.decode()


@pytest.mark.django_db
def test_address_string_representation(address):
    """Address string representation should be readable."""
    assert str(address) == '10 Main St'


@pytest.mark.django_db
def test_letting_string_representation(letting):
    """Letting string representation should equal title."""
    assert str(letting) == 'Test letting'
