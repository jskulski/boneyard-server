import pytest

from Boneyard import FlaskApp

def client():
    client = FlaskApp.app.test_client()
    return client

def test_can_get_home_page():
    response = client().get('/')

    print response.data

    assert response.status_code == 200

