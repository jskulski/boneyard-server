import pytest

import json

from Boneyard import FlaskApp

def client():
    client = FlaskApp.app.test_client()
    return client

def test_can_get_home_page():
    response = client().get('/')
    assert response.status_code == 200

def test_card_stack_is_empty_on_first_request():
    response = client().get('/card-stack')

    assert response.status_code == 200
    assert json.loads(response.data) == {}






