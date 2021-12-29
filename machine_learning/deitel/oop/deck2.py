# deck2.py
'''Deck version using the Card dataclass'''
import random
from carddataclass import Card

class DeckOfCards:
    NUMBER_OF_CARDS = 52 # constant number of cards

    def __init__(self) -> None:
        '''Initialize the deck'''
        self._current_card = 0 # idx of current card in self._deck
        self._deck = []

        for count in range(DeckOfCards.NUMBER_OF_CARDS):
            self._deck.append(Card(Card.FACES[count % 13], 
                                    Card.SUITS[count // 13])) 

    def shuffle(self):
        '''Shuffle deck.'''
        self._current_card = 0
        random.shuffle(self._deck)

    def deal_card(self):
        '''Return one Card'''
        try:
            card = self._deck[self._current_card]
            self._current_card += 1
            return card
        except:
            return None

    def __str__(self) -> str:
        '''Return a string representation of the current deck'''
        s = ''
        
        for index, card in enumerate(self._deck):
            s += f'{self._deck[index]:<19}'
            if (index + 1) % 4 == 0:
                s += '\n'
        
        return s