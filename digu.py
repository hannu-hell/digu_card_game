# Libraries
import random

# Constants

values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = ['hearts', 'clubs', 'spades', 'diamonds']


# Functions


def coin_toss(pick):
    toss = random.choice(['Heads', 'Tails'])
    if toss == pick:
        return True
    else:
        return False


def format_card(card):
    card = str(card)
    card = card.split(' ')
    formatted_card = Card(card[0], card[1])
    return formatted_card


def compare_cards(c1, c2):
    k = ["A", "K", "Q", "J"]
    if c1.value == "A" and c2.value == "A":
        return c1
    if c1.value == "A" and c2.value == "K":
        return c1
    if c1.value == "A" and c2.value == "Q":
        return c1
    if c1.value == "A" and c2.value == "J":
        return c1
    if c1.value == "K" and c2.value == "A":
        return c2
    if c1.value == "K" and c2.value == "K":
        return c1
    if c1.value == "K" and c2.value == "Q":
        return c1
    if c1.value == "K" and c2.value == "J":
        return c1
    if c1.value == "Q" and c2.value == "A":
        return c2
    if c1.value == "Q" and c2.value == "K":
        return c2
    if c1.value == "Q" and c2.value == "Q":
        return c1
    if c1.value == "Q" and c2.value == "J":
        return c1
    if c1.value == "J" and c2.value == "A":
        return c2
    if c1.value == "J" and c2.value == "K":
        return c2
    if c1.value == "J" and c2.value == "Q":
        return c2
    if c1.value == "J" and c2.value == "J":
        return c1
    if c1.value not in k and c2.value not in k:
        if int(c1.value) > int(c2.value):
            return c1
        if int(c1.value) == int(c2.value):
            return c1
        if int(c1.value) < int(c2.value):
            return c2
    if c1.value in k and c2.value not in k:
        return c1
    if c1.value not in k and c2.value in k:
        return c2

# Classes

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} {self.suit}"

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value


class Deck:
    def __init__(self):
        global values, suits
        self.deck = [Card(self.value, self.suit) for self.value in values for self.suit in suits]

    def __repr__(self):
        return self.deck

    def count(self):
        return len(self.deck)

    # This is a private method in the Deck class which should not be accessed but optimized by other
    # methods in this class. This method is called in the deal_card and deal_hand methods in this
    # class.

    def _deal(self, num):
        count = self.count()
        real = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.deck[-real:]
        self.deck = self.deck[:-real]
        return cards

    def deal_card(self):
        return self._deal(1)[0]  # as its a single card we access it with its index

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        random.shuffle(self.deck)
        return self


class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name} has a score of {self.score}"









