# redefine average

def average(*args):
    if not args:
        raise TypeError("average() missing 1 required positional argument.")
    else:
        return sum(args) / len(args)

