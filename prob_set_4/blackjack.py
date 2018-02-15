import random


class Card(object):
    """Card class, stores all values of a poker,
    gives the card value based on arguments (int)"""
    _values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10,
               'King': 10, 'Ace': (1, 11)}
    _rankList = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    _suitList = ['Spades', 'Clubs', 'Hearts', 'Diamonds']

    def __init__(self, suit, rank):
        self.suit = self._suitList[suit]
        self.rank = self._rankList[rank - 1]
        self.value = None
        self._get_value()

    def __repr__(self):
        return '{} of {}'.format(self.rank, self.suit)
    # # def _get_rank(self):
    #     return self.rank
    #
    # def _get_suit(self):
    #     return self.suit

    def _get_value(self):
        self.value = self._values[str(self.rank)]
        return self.value


class Hand(object):
    """docstring for Hand: add cards add several cards to hand
    current_value return the current value in hand, regardless of rules"""

    def __init__(self):
        self.cards = []
        self.value = [0]

    def add_cards(self, *add_cards):
        for card in add_cards:
            self.cards.append(card)

    def current_value(self):
        self.value = [0]
        aces = 0
        for card in self.cards:
            if 'Ace' in card.rank:
                self.value[0] += 1
                aces += 1
            else:
                self.value[0] += card.value
        for i in range(1, aces+1):
            self.value.append(self.value[0]+i*10)
        return self.value


class Player(object):
    """docstring for Player"""

    def __init__(self, first_name, last_name, purse):
        self.first_name = first_name
        self.last_name = last_name
        self.purse = purse
        self.hand = None


class Deck(object):
    """docstring for Deck"""

    def __init__(self):
        self.cards = None
        self.shuffle()

    def shuffle(self):
        self.cards = self.card_generator()

    def deal(self):
        try:
            return next(self.cards)
        except:
            return None

    def card_generator(self):
        generated = []
        for i in range(52):
            while True:
                card = Card(random.randrange(4), random.randrange(13))
                if (card.suit, card.rank) not in generated:
                    break
            generated.append((card.suit, card.rank))
            yield card
