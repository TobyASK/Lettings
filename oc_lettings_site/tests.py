"""Tests for project-level pages and handlers."""

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_returns_200(client):
    """Homepage should be reachable."""
    response = client.get(reverse('index'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_unknown_route_returns_custom_404(client):
    """Unknown URL should return custom 404 template."""
    response = client.get('/this-route-does-not-exist/')
    assert response.status_code == 404
    assert 'Sorry, this page does not exist.' in response.content.decode()
