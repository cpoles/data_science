def sum_of_multiples(limit, multiples):
    return sum([n for n in range(1, limit) if any(map(lambda x: n % x == 0 if x > 0 else False, multiples))])

