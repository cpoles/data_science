"""Nested Loops"""

# (a)
for l_number in range(1,11):
    for _ in range(l_number):
        print(f"{l_number * '*'}")
        break

# (b)
for l_number in range(10, 0, -1):
    for _ in range(l_number):
        print(f"{l_number * '*'}")
        break

# (c)
for l_number in range(10, 0, -1):
    for _ in range(l_number):
        print(f"{(l_number * '*'):>10}")
        break


# (d)
for l_number in range(1,11):
    for _ in range(l_number):
        print(f"{(l_number * '*'):>10}")
        break



