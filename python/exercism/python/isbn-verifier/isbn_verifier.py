import re

valid_chars = {"0": 0,
               "1": 1,
               "2": 2,
               "3": 3,
               "4": 4,
               "5": 5,
               "6": 6,
               "7": 7,
               "8": 8,
               "9": 9,
               "X": 10}


def is_valid(isbn):
    isbn = clear_string(isbn)
    # check length
    if len(isbn) != 10:
        return False

    # split first, middle and last
    first = isbn[0]
    middle = isbn[1:-1]
    last = isbn[-1]

    # check if first and middle are digits
    if not all(map(lambda x: x.isdigit(), first + middle)):
        return False

    # check if check digit is valid
    if last not in valid_chars.keys():
        return False

    return calc_isbn(isbn, valid_chars)


def clear_string(word):
    return re.sub(r'\W+', '', word)


def calc_isbn(isbn, char_map):
    coefs = [x for x in range(len(isbn), 0, -1)]
    nums = [char_map[char] for char in isbn]
    result = sum([coef * num for num, coef in zip(nums, coefs)])

    return result % 11 == 0
