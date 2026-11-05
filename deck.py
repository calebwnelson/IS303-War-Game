# Author: Caleb Nelson
'''Class: Deck
Attribute: cards (list of Card objects)
Methods: __init__(), shuffle(), draw_card(), add_cards(cards), card_count()
Creates a standard 52-card deck, shuffles, draws cards, and adds won cards to the bottom.'''


from card import Card
import random

class Deck:

    # Creates a deck of 52 cards
    def __init__(self):
        self.cards = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']:
                self.cards.append(Card(rank, suit))

    # Randomly reorders the deck
    def shuffle(self):
        random.shuffle(self.cards)

    # Draws the top card of the deck
    def draw_card(self):
        if self.cards:
            return self.cards.pop(0)
        # Returns None if the deck is empty. We'll want to build the game to accept this value as a win/loss
        else:
            return None

    # Add cards won in war to the deck
    def add_cards(self, cards):
        self.cards.extend(cards)

    # Return how many cards there are
    def card_count(self):
        return len(self.cards)