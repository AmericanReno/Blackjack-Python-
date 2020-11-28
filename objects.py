import random

class Card:
    def __init__(self):
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
        self.suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

    def getRanks(self):
        return list(self.ranks)

    def getSuits(self):
        return list(self.suits)

class Deck:
    def __init__(self, s, r):
        self.suits = s
        self.ranks = r
        self.deck = []

        for i in self.suits:
            for j in self.ranks:
                card = []
                card.append(j)
                card.append(i)
                self.deck.append(card)
                
    def shuffle(self):
        return random.shuffle(self.deck)

    def count(taken):
        counter = 1
        for card in deck:
            for i in card:
                counter += 1
        return counter - taken

    def getDeck(self):
        return self.deck
