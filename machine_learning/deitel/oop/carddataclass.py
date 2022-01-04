# carddataclass.py

'''Card data class with class attributes, data attributes,
    autogenerated methods and explicitly defined methods.'''

from dataclasses import dataclass
from typing import ClassVar, List

@dataclass
class Card:
    
    # class attributes
    FACES: ClassVar[List[str]] = ['Ace', '2', '3', '4', '5', '6', '7',
                                    '8', '9', '10', 'Jack', 'Queen', 'King']
    
    SUITS: ClassVar[List[str]] = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    # data attributes
    face: str
    suit: str

    @property
    def image_name(self):
        '''Return the Card's image file name.'''
        return str(self).lower().replace(' ', '_') + '.png'

    def __str__(self) -> str:
        '''Return string represenattion for str()'''
        return f'{self.face} of {self.suit}'
    
    def __format__(self, format: str) -> str:
        '''Return formatted string representation.'''
        return f'{str(self):{format}}'