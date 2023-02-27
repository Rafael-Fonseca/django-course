from django.test import Client
from django.urls import reverse
import pytest
from pypro.django_assertions import assert_contains


@pytest.fixture
def response(client: Client):
    return client.get(reverse('base:home'))


def test_status_code(response):
    assert response.status_code == 200


def test_title(response):
    assert_contains(response, '<title>MEU</title>')


def test_home_link(response):
    assert_contains(response, f'href="{reverse("base:home")}">Python Pro</a>')
