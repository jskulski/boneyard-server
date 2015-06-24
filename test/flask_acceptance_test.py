import sys, os
test_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, test_directory + '/../')

import json

from Boneyard import FlaskApp

FlaskApp.app.testing = True
FlaskApp.app.debug = True

def client():
    client = FlaskApp.app.test_client()
    return client

def test_cards_returns_json():
    response = client().get('/cards')
    assert response.mimetype == 'application/json'

def test_card_stack_is_empty_on_first_request():
    response = client().get('/cards')

    assert response.status_code == 200
    assert json.loads(response.data) == dict(
        cards=[]
    )

def test_creating_a_card_results_in_a_list_with_that_card():
    expected_body = "This is the content of the card"
    response = client().post('/card', data=dict(
        body=expected_body
    ), follow_redirects=True)

    assert response.status_code == 200
    assert json.loads(response.data) == {
        'cards': [
            {'body': expected_body}
        ]
    }

