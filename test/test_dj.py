import pytest


# testowanie widokóœ
@pytest.mark.django_db
def test_base_view(client):
    results = client.get("/")
    assert results.status_code == 200


@pytest.mark.django_db
def test_genres_view(client):
    results = client.get("/genres/")
    assert results.status_code == 200


@pytest.mark.django_db
def test_games_view(client):
    results = client.get("/games/")
    assert results.status_code == 200


@pytest.mark.django_db
def test_publishers_view(client):
    results = client.get("/publishers/")
    assert results.status_code == 200


@pytest.mark.django_db
def test_platforms_view(client):
    results = client.get("/platforms/")
    assert results.status_code == 200


# testowanie user profile

@pytest.mark.django_db
def test_logged_user_profile(client, user):
    client.login(username='tester', password='tymczasowe')
    result = client.get('/user/{}'.format(user.id))
    assert result.status_code == 200


# testowanie modeli

@pytest.mark.django_db
def test_genres_user(client, user, genres):
    client.login(username='tester', password='tymczasowe')
    result = client.get('/genres/')
    assert result.status_code == 200
    assert len(genres) == len(result.context['objects'])
    for genre in genres:
        assert genre in result.context['objects']


@pytest.mark.django_db
def test_publisher_user(client, user, publishers):
    client.login(username='tester', password='tymczasowe')
    result = client.get('/publishers/')
    assert result.status_code == 200
    assert len(publishers) == len(result.context['objects'])
    for publisher in publishers:
        assert publisher in result.context['objects']
