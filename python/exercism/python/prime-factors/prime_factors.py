def factors(value):
    primes = []
    prime = 2
    while True:
     if value == 1:
         break
     if value % prime == 0:
         value = value // prime
         primes.append(prime)
     else:
         prime = prime + 1

    return primes
