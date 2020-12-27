"""Table of Squares and Cubes"""

print('number\tsquare\t  cube')

for number in range(6):
    print(f'{number:>6}\t{number**2:>6}\t{number**3:>6}')
