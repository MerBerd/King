import random

class Card:
    def __init__(self, suit, magnitude, value=False):
        self.is_trump = value
        self.suit = suit
        self.magnitude = magnitude

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, suit):
        if not suit in ['♠️','♣️','♥️','♦️']:
            raise ValueError('Invalid suite')
        self._suit = suit

    @property
    def magnitude(self):
        return self._magnitude

    @magnitude.setter
    def magnitude(self, magnitude):
        if not isinstance(magnitude, int):
            raise ValueError('Invalid error')
        self._magnitude = magnitude
    
    @property
    def is_trump(self):
        return self._is_trump
    
    @is_trump.setter
    def is_trump(self, value):
        if not isinstance(value, bool):
            raise ValueError('Invalid error')
        self._is_trump = value
    
    def __str__(self):
        return f'{self.magnitude}{self.suit}'

            
class CardDeck:
    def __init__(self):
        self.cards = []
    
    def generate_deck(self):
        for suit in ['♠️','♣️','♥️','♦️']:
            for magnitude in range(7, 15):
                self.cards.append(Card(suit, magnitude))

    def __str__(self):
        for card in self.cards:
            return f'{card.magnitude} {card.suit}'


class Player:
    def __init__(self, number):
        self.card_set = []
        self.number = number
    
    def set_cards(self, card):
        self.card_set.append(card)


def generate_players(player_count, deck):
    random.shuffle(deck.cards)
    player_list = [Player(i+1) for i in range(player_count)]
    while deck.cards:
        for player in player_list:
            player.set_cards(deck.cards.pop())
    
    return player_list


deck = CardDeck()
deck.generate_deck()
players = generate_players(4, deck)

for player in players:
    print(player.number)
    for card in player.card_set:
        print(card, end=' ')
    print()

    







