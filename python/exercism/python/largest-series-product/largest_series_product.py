from curses.ascii import isalpha, isascii
from functools import reduce

def largest_product(series, size):
    if (series or not series) and size == 0:
        return 1

    if size > len(series):
        raise ValueError("span must be smaller than string length") 
    elif size <= 0:
        raise ValueError("span must be greater than zero")

    if any([isalpha(x) for x in series]):
        raise ValueError("digits input must only contain digits")

    all_series = []
    while True:
        if len(series) == size:
            all_series.append(series)
            break
        else:
            digits = series[:size]
            all_series.append(digits)
            series = series[1:]
        
    return max(list(map(lambda u: reduce(lambda x, y: int(x) * int(y), u), all_series)))