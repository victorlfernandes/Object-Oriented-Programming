class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def getValue(self):
        return self.value

    def getSuit(self):
        return self.suit

    def __str__(self):
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, ' J', ' Q', ' K', ' A']
        if self.suit == 0:
            return '{:2} ♥'.format(cards[self.value - 2])
        if self.suit == 1:
            return '{:2} ♣'.format(cards[self.value - 2])
        if self.suit == 2:
            return '{:2} ♦'.format(cards[self.value - 2])
        if self.suit == 3:
            return '{:2} ♠'.format(cards[self.value - 2])