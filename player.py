#Player class (player.py)
from deck import Deck

#creates a player class with a name and a deck of cards
class Player:
    def __init__(self, name):
        self.name = name
        self.deck = Deck()
    #plays a card from the player's deck, returning it if available
    def play_card(self):
        if self.has_cards():
            return self.deck.draw_card()
        return None

    #collects cards into the player's deck
    def collect_cards(self, cards):
        self.deck.add_cards(cards)

    #returns the number of cards in the player's deck
    def card_count(self):
        return self.deck.card_count()

    #returns True if the player has cards, False otherwise
    def has_cards(self):
        return self.deck.card_count() > 0
    