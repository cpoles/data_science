def square_root(number):
    if number == 1:
        return number
    
    guess = number // 2

    while number // guess != guess:
        guess -=1
    
    return guess
