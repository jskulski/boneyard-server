from Card import Card
from Card import CardStack

def get_new_card():
    return Card(id=1)
    pass

def create_card(title, body):
    card = Card(id=1, title=title, body=body)
    return card

def get_card_stack():
    return CardStack()