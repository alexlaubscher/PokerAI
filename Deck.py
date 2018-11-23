import random
from Card import Card

class Deck:
    #constructs deck of all 52 cards
    def __init__(self):
        self.suits = ["S","C","D","H"]
        self.values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        self.deck = {}
        for suit in self.suits:
            for value in self.values:
                string = str(value) + suit
                self.deck[string] = 1

    #gets top card on deck and removes it from deck
    def getTopCard(self):
        topCard = self.deck[0]
        del self.deck[0]
        return topCard

    def genCard(self):
      while True:
        suit = random.choice(self.suits)
        value = random.choice(self.values)
        string = str(value) + suit
        if self.deck[string] == 1:
          self.deck[string] = 0
          return Card(value, suit)
    
    def setDict(self, string):
      self.deck[string] = 0

    #returns the # of cards left in the deck
    def getCardsLeft(self):
        return len(self.deck)

    #shuffles the deck
    def shuffle(self):
        random.shuffle(self.deck)

    def __str__(self):
        return self.deck
