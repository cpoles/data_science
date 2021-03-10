"""List compreheension for inches -> meters conversion"""


def in_to_met(inches):
    '''Converts inches to meters'''
    return inches * 0.0254


def inches_to_meters(inches_list):
    '''Converts inches to meters using list comprehension'''
    return [(inch, in_to_met(inch)) for inch in inches_list]


def inches_to_meters2(inches_list):
    '''Converts inches to meters using a map call'''
    return list(map(lambda x: (x, in_to_met(x)), inches_list))


inches_to_meters([69, 77, 54])

inches_to_meters2([69, 77, 54])
