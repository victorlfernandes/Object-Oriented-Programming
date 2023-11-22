class Score:

    def __init__(self):
        self.totalScore = 200
        self.hand = 0
        self.frequency = 0

    def setHand(self, hand):
        self.hand = hand
        self.frequency = self.countCards()

    def getScore(self):
        return self.totalScore

    def round(self, bet):
        if bet < 0 or bet > self.totalScore:
            return -1
        plays = []
        plays.append([self.royalStraightFlush(), 200])
        plays.append([self.straightFlush(), 100])
        plays.append([self.fourOfaKind(), 50])
        plays.append([self.fullHand(), 20])
        plays.append([self.flush(), 10])
        plays.append([self.straight(), 5])
        plays.append([self.threeOfaKind(), 2])
        plays.append([self.twoPairs(), 1])
        index = -1
        for i in range(plays.__len__()):
            if plays[i][0] == True:
                index = i
                break
        if index == -1:
            self.totalScore -= bet  
        else:
            self.totalScore += bet * plays[index][1]

    def countCards(self):
        values = 13 * [0]
        for i in range(5):
            values[self.hand.cards[i].getValue() - 2] += 1
        return values

    # returns true if cards are from the same suit
    def checkSuits(self):
        suit = self.hand.cards[0].getSuit()
        for i in range(1, 5):
            if self.hand.cards[i].getSuit() != suit:
                return False
        return True

    # returns true if it is a sequence
    def checkSequence(self):
        index = self.hand.getMinValue() - 2
        for i in range(index + 1, index + 5):
            if self.frequency[i] != 1:
                return False  
        return True          

    def twoPairs(self):
        pairCounter = 0
        for i in range(13):
            if self.frequency[i] == 2:
                pairCounter += 1
        if pairCounter == 2:
            return True
        else:
            return False

    def threeOfaKind(self):
        triplet = False
        for i in range(13):
            if self.frequency[i] == 3:
                triplet = True
        return triplet

    def straight(self):
        return self.checkSequence() and not self.checkSuits()

    def flush(self):
        return not self.checkSequence() and self.checkSuits()

    def fullHand(self):
        pair = False
        triplet = False
        for i in range(13):
            if self.frequency[i] == 2:
                pair = True
            if self.frequency[i] == 3:
                triplet = True
        return pair and triplet

    def fourOfaKind(self):
        for i in range(13):
            if self.frequency[i] == 4:
                return True
        return False

    def straightFlush(self):
        return self.checkSequence() and self.checkSuits()

    def royalStraightFlush(self):
        index = self.hand.getMinValue() - 2
        return self.straightFlush() and index == 8
