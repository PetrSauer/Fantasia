"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

def value_of_card(card):
    #Cards and their value in BlackJack
    if card in ('J', 'K', 'Q'):
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)
        
    pass


def higher_card(card_one, card_two):
    
    def value_of_card(card):
            if card in ('J', 'K', 'Q'):
                return 10
            elif card == 'A':
                return 1
            else:
                return int(card)
                
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    
    if value_one > value_two:
        return card_one
    elif value_two > value_one:
        return card_two
    else:
        return card_one, card_two
    
    pass


def value_of_ace(card_one, card_two):

    def value_of_card(card):
        if card in ('J', 'K', 'Q'):
            return 10
        elif card == 'A':
            return 11
        else:
            return int(card)
                
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one + value_two <= 10: 
        return 11
    else:
        return 1

    pass


def is_blackjack(card_one, card_two):


    def value_of_card(card):
        if card in ('J', 'K', 'Q'):
            return 10
        elif card == 'A':
            return 11
        else:
            return int(card)
                
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one + value_two == 21:
        return True
    else:
        return False


    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    pass


def can_split_pairs(card_one, card_two):


    def value_of_card(card):
        if card in ('J', 'K', 'Q'):
            return 10
        elif card == 'A':
            return 11
        else:
            return int(card)
                
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one == value_two:
        return True
    else:
        return False

    pass


def can_double_down(card_one, card_two):


    def value_of_card(card):
        if card in ('J', 'K', 'Q'):
            return 10
        elif card == 'A':
            return 11
        else:
            return int(card)
                
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    total = value_one + value_two
    if total > 11 and (card_one == 'A' or card_two == 'A'):
        total -= 10
        
    return 9 <= total <= 11
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    pass
