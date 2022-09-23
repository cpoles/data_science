def steps(number):
    if number <= 0:
        raise ValueError('Only positive integers are allowed')
    n_steps = 0
    while True:
        if number == 1:
            break

        if number % 2 == 0:
            number /= 2
        else:
            number = 3 * number + 1

        n_steps += 1
    return n_steps
