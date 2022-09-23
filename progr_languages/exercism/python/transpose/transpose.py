def transpose(lines):
    if not lines:
        return ''

    lines = lines.split('\n')
    # get the longest string in the list
    max_len = max([len(line) for line in lines])
    min_len = min([len(line) for line in lines])
    print(min_len)
    # pad all strings with spaces to match same size
    lines = [line.ljust(max_len) for line in lines]
    # zip all elements of the list
    lines = list(map(lambda x: ''.join(x), zip(*lines)))
    lines[min_len:] = list(map(lambda x: x.rstrip(), lines[min_len:]))

    return '\n'.join(lines)


