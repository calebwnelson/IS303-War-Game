# main.py - Game logic for Two-Deck War
import random
from player import Player


def play_round(player1, player2):
    """Play one round (including any wars) and return the winning Player."""
    card1 = player1.play_card()
    card2 = player2.play_card()
    pot = [card1, card2]  # every card played this round
    print(f"{player1.name} drew the {card1.get_description()}.")
    print(f"{player2.name} drew the {card2.get_description()}.")

    # Tie: go to war until someone wins (or a player runs out of cards)
    while card1.value == card2.value and player1.has_cards() and player2.has_cards():
        print("War!")
        card1 = player1.play_card()
        card2 = player2.play_card()
        pot.extend([card1, card2])
        print(f"{player1.name} drew the {card1.get_description()}.")
        print(f"{player2.name} drew the {card2.get_description()}.")

    # Higher card wins; if still tied, the player who ran out loses
    if card1.value > card2.value:
        winner = player1
    elif card2.value > card1.value:
        winner = player2
    elif player1.has_cards():
        winner = player1
    else:
        winner = player2

    # Shuffle the pot so a game can't loop forever, then give it to the winner
    random.shuffle(pot)
    winner.collect_cards(pot)

    result = "war" if len(pot) > 2 else "round"
    print(f"{winner.name} wins the {result}!")
    return winner


def play_game():
    """Create the players, play rounds until one has every card, announce the winner."""
    print("Welcome to Two-Deck War!")

    player1 = Player("Player 1")
    player2 = Player("Player 2")
    player1.deck.shuffle()
    player2.deck.shuffle()

    while player1.has_cards() and player2.has_cards():
        play_round(player1, player2)
        print(f"{player1.name} has {player1.card_count()} cards.")
        print(f"{player2.name} has {player2.card_count()} cards.")
        if player1.has_cards() and player2.has_cards():
            input("Press Enter to play the next round.\n")

    winner = player1 if player1.has_cards() else player2
    print(f"{winner.name} has collected all of the cards.")
    print(f"{winner.name} wins the game!")


if __name__ == "__main__":
    play_game()
