"""Aproximating Mathematical Constant e"""

e = 1


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


for n in range(1, 11):
    e += 1 / factorial(n)

print(e)
