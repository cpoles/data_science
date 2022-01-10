import re
from string import ascii_lowercase, punctuation

ALPHABET = list(ascii_lowercase)

def is_pangram(sentence):
    sentence = re.sub(r'[0-9 _.,!"\'\/$]*', '', sentence.lower())
    return sorted(list(set(sentence))) == ALPHABET
