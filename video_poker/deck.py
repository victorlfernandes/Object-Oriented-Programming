import random
from card import Card

class Deck:

    def __init__(self):
        self.deck = []
        self.deckSize = 0
        for i in range(4):
            for j in range(2, 15):
                self.deck.append(Card(i, j))
                self.deckSize += 1
        random.shuffle(self.deck)

    def getCard(self):
        self.deckSize -= 1
        return self.deck.pop()

    def __str__(self):
        str = ''
        for i in range(self.deckSize):
            str += self.deck[i].__str__() + '\n'
        return str[:-1]
