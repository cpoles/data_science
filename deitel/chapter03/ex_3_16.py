"""Nested Control Statements"""

largest = 0
snd_largest = largest

for _ in range(10):
    number = int(input('Enter a number: '))
    if number > largest:
        snd_largest = largest
        largest = number

print(f'The largest number is { largest } and the second largest is {snd_largest}')
