from deck import Deck

class Hand:

    def __init__(self):
        self.deck = Deck()
        self.cards = []
        self.amtOfCards = 5
        for i in range(self.amtOfCards):
            self.cards.append(self.deck.getCard())

    def getHand(self):
        return self.cards
    
    def getMinValue(self):
        min = self.cards[0].getValue()
        for i in range(1, self.amtOfCards):
            if self.cards[i].getValue() < min:
                min = self.cards[i].getValue()
        return min

    def boolChangeHand(self, cardsToChange = None):
        if cardsToChange == None:
            cardsToChange = self.amtOfCards * [True]
        for i in range(self.amtOfCards):
            if cardsToChange[i] == True:
                self.cards[i] = self.deck.getCard()

    def changeHand(self, cardsToChange = None):
        if cardsToChange == None:
            self.boolChangeHand()
            return
        b = self.amtOfCards * [False]
        s = cardsToChange.split()
        for i in s:
            index = int(i) - 1
            if index >= 0 and index < self.amtOfCards:
                b[index] = True
        self.boolChangeHand(b)

    def __str__(self):
        str = '1       2       3       4       5\n'
        str += '+-----+ ' * self.amtOfCards
        str += '\n'
        str += '|     | ' * self.amtOfCards
        str += '\n'
        for i in range(self.amtOfCards):
            str += '|'
            str +=  self.cards[i].__str__() 
            str += ' | '
        str += '\n'
        str += '|     | ' * self.amtOfCards
        str += '\n'
        str += '+-----+ ' * self.amtOfCards
        return str
