import pytest

import json

from Boneyard import FlaskApp

def client():
    client = FlaskApp.app.test_client()
    return client

def test_card_stack_is_empty_on_first_request():
    response = client().get('/cards')

    assert response.status_code == 200
    assert json.loads(response.data) == {}

def test_we_can_post_to_create_a_new_card():
    response = client().post('/card', data=dict(
        body="This is the body of the card"
    ))

    assert response.status_code == 200







