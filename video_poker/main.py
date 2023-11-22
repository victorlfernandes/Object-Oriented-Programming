from hand  import Hand
from score import Score

playing = True
round = 1
score = Score()

while playing:

    print('Round {}'.format(round))
    print('You own {}'.format(score.getScore()))

    hand = Hand()
    print('\nYour hand:\n{}'.format(hand))

    change = input('Which cards do you want to change? ')
    hand.changeHand(change)

    print('\nYour hand:\n{}'.format(hand))
    change = input('Which cards do you want to change? ')
    hand.changeHand(change)

    score.setHand(hand)

    print('\nYour hand:\n{}'.format(hand))
    
    invalidBet = True
    while invalidBet:
        bet = int(input('How much do you want to bet? '))
        aux = score.round(bet)
        if aux == -1:
            print('Invalid bet, try again')
        else:
            invalidBet = False

    print()
    if score.getScore() <= 0:
        print('You broke')
        playing = False
    else:
        print('You own {}'.format(score.getScore()))
        str = input('Do you want to keep playing? (y/n) ')
        if str == 'n':
            playing = False
        else:
            round += 1
            print()
        
