def score(x, y):
    '''Using the pythagorean theorem:

        The center of the circles are at (0,0)

        Should satisfy

        (x ** 2 + y ** 2) <= r ** 2 (the radius for the circle reward)

    '''
    squared_dist = x ** 2 + y ** 2

    if squared_dist <= 1 ** 2:
        return 10
    elif squared_dist <= 5 ** 2:
        return 5
    elif squared_dist <= 10 ** 2:
        return 1
    else:
        return 0
