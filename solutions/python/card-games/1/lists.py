def get_rounds(number):
    """

     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """
    rounds = [number + i for i in range(3)]
    return rounds


def concatenate_rounds(rounds_1, rounds_2):
    """

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    rounds_1.extend(rounds_2)
    return rounds_1




def list_contains_round(rounds, number):
    """

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """
    return number in rounds


def card_average(hand):
    """

    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """
    num_cards = sum(hand)
    return num_cards / len(hand) if hand else 0.0
    


def approx_average_is_average(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - if approximate average equals to the `true average`.
    """
    fst = hand[0]
    lst = hand[-1]
    avg_1 = (fst + lst) /2 
    median = hand[len(hand)//2]
    card_avg = card_average(hand)
    return avg_1 == card_avg or median == card_avg
    


def average_even_is_average_odd(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_cards = [card for card in hand[0 : : 2]]
    odd_cards = [card for card in hand[1 : : 2]]
    even_avg = 0
    odd_avg = 0
    if even_cards:
        even_avg = sum(even_cards) / len(even_cards)
    if odd_cards:
        odd_avg = sum(odd_cards) / len(odd_cards)
    return even_avg == odd_avg


def maybe_double_last(hand):
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value double
    """
    return hand[:-1] + [22] if hand[-1] == 11 else hand
