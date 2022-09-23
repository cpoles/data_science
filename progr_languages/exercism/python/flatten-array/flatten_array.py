def flatten(list_of_lists):
    # base case
    if not list_of_lists:
        return list_of_lists

    head, *tail = list_of_lists

    if head is None:
        return flatten(tail)
    else:
        if isinstance(head, list):
            return flatten(head) + flatten(tail)
        return [head] + flatten(tail)
