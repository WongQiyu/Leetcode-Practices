from collections import deque
import random
import itertools


def shuffle_cards_method_1(cards):
    res = deque([])
    i = 0
    while i < len(cards):
        res.insert(0, cards[i])
        i += 1
        if i < len(cards):
            res.append(cards[i])
        i += 1
    return list(res)


def shuffle_cards_method_2(cards):
    even = cards[::2]
    odd = cards[1::2]
    return even[::-1] + odd


def main():
    numeric_cards = list(range(15))
    shuffled_cards_1 = shuffle_cards_method_1(numeric_cards)
    shuffled_cards_2 = shuffle_cards_method_2(numeric_cards)
    print(shuffled_cards_1)
    print(shuffled_cards_2)
    assert shuffled_cards_1 == shuffled_cards_2

    CARD_VALUES = [
        "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "Jack", "Queen", "King", "Ace",
    ]
    CARD_COLORS = ["Spades", "Hearts", "Clubs", "Diamonds"]
    cards_pack = [
        f"{value} of {color}"
        for value, color
        in itertools.product(CARD_VALUES, CARD_COLORS)
    ]
    random.shuffle(cards_pack)
    shuffled_cards_pack_1 = shuffle_cards_method_1(cards_pack)
    shuffled_cards_pack_2 = shuffle_cards_method_2(cards_pack)
    assert shuffled_cards_pack_1 == shuffled_cards_pack_2


if __name__ == "__main__":
    main()