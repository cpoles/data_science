def transpose(lines):
    if not lines:
        return "\n".join(lines)

    lines = lines.split('\n')
    # get the longest string in the list
    max_len = max([len(line) for line in lines])
    min_len = min([len(line) for line in lines])
    print(min_len)
    # pad all strings with spaces to match same size
    lines = [line.ljust(max_len) for line in lines]
    # zip all elements of the list
    lines = list(map(lambda x: ''.join(x), zip(*lines)))

    # length of the largest line containing the penultimate period at the end of the line
    mlen = 0
    
    for idx, line  in enumerate(lines):
        if line[-1] == '.':
            mlen = len(line)
            for i in range(idx+1, len(lines)):
                lines[i] = lines[i][:-1]
        
        if line == lines[-1]:
            lines[-1] = line.rstrip()

    for idx, line in enumerate(lines):
        if all([c == " " for c in line]):
            continue

        if len(line) > len(lines[-1]) and len(line) < mlen:
            lines[idx] = line.rstrip()


    return "\n".join(lines)