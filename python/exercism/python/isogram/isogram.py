def is_isogram(string):
    string = string.lower()
    # remove space and hyphens
    string = [char for char in string if char not in [' ', '-']]

    return len(string) == len(set(string))