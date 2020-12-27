"""Aproximating Mathematical Constant Pi"""

initial = 4
terms = 1
pi = 0
n = 1

while pi <= 3.141519:
    print(f'({n}, {n+2})')
    pi += (initial / n) - (initial / (n+2))
    n = n + initial
    terms += 4

print(f'Number of terms: {terms} for pi = {pi:.6f}')

