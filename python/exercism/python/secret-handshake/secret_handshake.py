def commands(binary_str):
    handshakes = ["reverse", "jump", "close your eyes", "double blink", "wink"]
    bins = [int(digit) for digit in binary_str]

    result = [handshake for n, handshake in zip(bins, handshakes) if n == 1]

    if 'reverse' in result:
        return result[1:]
    else:
        return result[::-1]
