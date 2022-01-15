def is_armstrong_number(number):
    digits = str(number)
    return sum([int(digit)**len(digits) for digit in digits]) == number
