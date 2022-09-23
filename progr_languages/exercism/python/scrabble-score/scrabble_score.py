def points(letter):
    if letter in ['A','E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']:
        return 1
    if letter in ['D', 'G']:
        return 2
    if letter in ['B', 'C', 'M', 'P']:
        return 3
    if letter in ['F','H','V','W','Y']:
        return 4
    if letter in ['K']:
        return 5
    if letter in ['J', 'X']:
        return 8
    if letter in ['Q', 'Z']:
        return 10

def score(word):
    return sum([points(char) for char in word.upper()])
