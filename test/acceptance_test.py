import sys, os
test_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, test_directory + '/../')

import Boneyard
from Boneyard.Card import Card
from Boneyard.Card import CardStack

def test_can_create_new_card():
    card = Card(id=1)

def test_can_create_new_card_with_title_and_text():
    card = Card(
        id=1,
        title='This is a title',
        body='this is the text'
    )
    assert isinstance(card, Card)

def test_we_can_request_a_new_card_from_the_boneyard():
    card = Boneyard.get_new_card()
    assert isinstance(card, Card)

def test_new_card_has_id_of_one():
    card = Boneyard.get_new_card()
    assert card.id == 1

def test_we_can_create_a_new_card_with_title_text():
    expected_title = 'Title!'
    expected_body  = 'Text!'
    card = Boneyard.create_card(title=expected_title, body=expected_body)

    assert card.title == expected_title
    assert card.body == expected_body

def test_initial_card_stack_is_empty():
    card_stack = Boneyard.get_card_stack()

    assert card_stack.is_empty()
