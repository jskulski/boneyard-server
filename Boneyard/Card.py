class CardStack:
    def __init__(self, cards=[]):
        """
        :param cards: list[Card]
        """
        self.cards = cards

class Card:
    def __init__(self, id, title=None, body=None):
        self.id = 1
        self.title = title
        self.body = body
