
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

        # Face cards rank above numbered cards, and Ace is highest.
        if rank == "Jack":
            self.value = 11
        elif rank == "Queen":
            self.value = 12
        elif rank == "King":
            self.value = 13
        elif rank == "Ace":
            self.value = 14
        else:
            self.value = int(rank)

    def get_description(self):
        return f"{self.rank} of {self.suit}"
