import math
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    factors = [divisor for divisor in list(range(1, number // 2 + 1)) if number % divisor == 0]

    if sum(factors) == number:
        return 'perfect'
    elif sum(factors) > number:
        return 'abundant'
    else:
        return 'deficient'
