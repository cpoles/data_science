# deck.py
'''Deck class represents a deck of Cards'''
import random
from card import Card

class DeckOfCards:
    NUMBER_OF_CARDS = 52 # constant number of cards

    def __init__(self) -> None:
        '''Initialize the deck'''
        self._current_card = 0
        self._deck = []

        for count in range(DeckOfCards.NUMBER_OF_CARDS):
            self._deck.append(Card(Card.FACES[count % 13], 
                                    Card.SUITS[count // 13])) 