NUMBERS = {
    1: ('first', 'a Partridge in a Pear Tree.'),
    2: ('second', 'two Turtle Doves'),
    3: ('third', 'three French Hens'),
    4: ('fourth', 'four Calling Birds'),
    5: ('fifth', 'five Gold Rings'),
    6: ('sixth', 'six Geese-a-Laying'),
    7: ('seventh', 'seven Swans-a-Swimming'),
    8: ('eighth', 'eight Maids-a-Milking'),
    9: ('ninth', 'nine Ladies Dancing'),
    10: ('tenth', 'ten Lords-a-Leaping'),
    11: ('eleventh', 'eleven Pipers Piping'),
    12: ('twelfth', 'twelve Drummers Drumming')
}

def gifts(end_verse):
    _, gift = NUMBERS[end_verse]

    if end_verse == 2:
        return gift + ', and ' + gifts(end_verse-1)
    
    if end_verse == 1:
        return gift

    return gift + ', ' + gifts(end_verse-1)

def recite(start_verse, end_verse):
    ordinal, _ = NUMBERS[end_verse]

    lyrics = f"On the {ordinal} day of Christmas my true love gave to me: "

    gifts_part = gifts(end_verse)

    if start_verse == end_verse:
        return [lyrics + gifts_part]

    return recite(start_verse, end_verse - 1) + [lyrics + gifts_part]