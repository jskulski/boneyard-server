import pytest

import json

from flask import Response
from Boneyard import FlaskApp

FlaskApp.app.testing = True
FlaskApp.app.debug = True

def client():
    client = FlaskApp.app.test_client()
    return client

def test_card_stack_is_empty_on_first_request():
    response = client().get('/cards')

    assert response.status_code == 200
    assert json.loads(response.data) == {}

def test_creating_a_card_redirects_to_card_stack_and_includes_the_created_card():
    expected_body = "This is the content of the card"
    response = client().post('/card', data=dict(
        body=expected_body
    ), follow_redirects=True)

    assert response.status_code == 200
    assert expected_body in response.data







