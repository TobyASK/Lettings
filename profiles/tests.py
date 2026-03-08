"""Tests for profiles app."""

import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from profiles.models import Profile


@pytest.fixture
def profile_obj(db):
    """Create a profile fixture."""
    user = User.objects.create_user(username='alice', password='Abc1234!')
    return Profile.objects.create(user=user, favorite_city='Paris')


@pytest.mark.django_db
def test_profiles_index_returns_200(client, profile_obj):
    """The profiles list page should return HTTP 200."""
    response = client.get(reverse('profiles_index'))
    assert response.status_code == 200
    assert 'alice' in response.content.decode()


@pytest.mark.django_db
def test_profile_detail_returns_200(client, profile_obj):
    """The profile detail page should return HTTP 200."""
    response = client.get(
        reverse('profile', kwargs={'username': profile_obj.user.username})
    )
    assert response.status_code == 200
    assert 'Paris' in response.content.decode()


@pytest.mark.django_db
def test_profile_string_representation(profile_obj):
    """Profile string representation should equal username."""
    assert str(profile_obj) == 'alice'
