import pytest
from django.contrib.auth.models import User
from django.test import Client

from games.models import Genre, Publisher


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def user():
    u = User()
    u.username = 'tester'
    u.set_password('tymczasowe')
    u.save()
    return u


@pytest.fixture
def genres():
    genres = []
    for x in range(10):
        genres.append(Genre.objects.create(name='genre_{x}'))
    return genres


@pytest.fixture
def publishers():
    publishers = []
    for x in range(10):
        publishers.append(Publisher.objects.create(name='genre_{x}', country='country_{x}'))
    return publishers
