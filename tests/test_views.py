from datetime import datetime, timedelta
import pytest

from booking.app import app
from booking.models import Event
from booking import storage

@pytest.fixture
def client():
    client = app.test_client()
    yield client


@pytest.fixture(autouse=True)
def run_around_tests():
    del storage.app.storage
    yield


def test_events_empty_list(client):
    with app.app_context():
        rv = client.get('/events', content_type='application/json')
    assert rv.json == []
    assert rv.headers['Content-Type'] == 'application/json'


def test_events_list(client):
    now = datetime.now()
    event = Event('Opener', 400, 100, now + timedelta(days=10), now)
    with app.app_context():
        storage.get_storage().add_event(event)
        rv = client.get('/events', content_type='application/json')
    data = rv.json
    assert isinstance(data, list)
    assert len(data) == 1
    assert rv.headers['Content-Type'] == 'application/json'


def test_events_detail_doesnt_exist(client):
    with app.app_context():
        rv = client.get('/event/nonexistent')
    assert rv.status_code == 400


def test_events_detail(client):
    now = datetime.now()
    event = Event('Opener', 400, 100, now + timedelta(days=10), now)
    with app.app_context():
        storage.get_storage().add_event(event)
        rv = client.get('/event/' + event.id, content_type='application/json')
        assert rv.headers['Content-Type'] == 'application/json'
        assert rv.status_code == 200
        assert rv.json['id'] == event.id
