"""Arbitrary argument list"""


def product(*args):
    """Calculate the product of a series of integers"""
    total = 1
    for number in args:
        total *= number
    return total
