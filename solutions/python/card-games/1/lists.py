"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    return  [number, number + 1, number + 2]


    
    pass


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    return rounds_1 + rounds_2
    
    pass


def list_contains_round(rounds, number):
    """
    Returns True if the 'number' is inside the 'rounds' list, 
    otherwise returns False.
    """
    
    """Check if the list of rounds contains the specified number.
    
    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    return number in rounds
    pass


def card_average(hand):
    return  sum(hand) / len(hand)
   
    pass


def approx_average_is_average(hand):
    actual_avg = sum(hand) / len(hand)
    
    # Strategy 1: 
    first_last_avg = (hand[0] + hand[-1]) / 2
    
    # Strategy 2: The median (middle card)
    median = hand[len(hand) // 2]
    
    # Return 
    return actual_avg == first_last_avg or actual_avg == median
    pass


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    actual_avg = sum(hand) / len(hand)
    median = hand[len(hand) // 2]
    return actual_avg == median
    
    pass


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = 22

    return hand
    pass
