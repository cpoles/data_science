def equilateral(sides):
    s1, s2, s3 = sides
    if validate(sides):
        return True if s1 == s2 and \
                       s2 == s3 else False
    return False


def isosceles(sides):
    s1, s2, s3 = sides
    if validate(sides):
        return True if s1 == s2 or \
                       s2 == s3 or \
                       s1 == s3 else False
    return False


def scalene(sides):
    s1, s2, s3 = sides
    if validate(sides):
        return True if s1 != s2 and \
                       s2 != s3 else False
    return False


def validate(sides):
    s1, s2, s3 = sides
    if all(map(lambda x: x > 0, sides)):
        if s1 + s2 >= s3 and s2 + s3 >= s1 and s1 + s3 >= s2:
            return True
    return False
