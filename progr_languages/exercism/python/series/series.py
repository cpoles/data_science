def slices(series, length):
    validate_slices(series, length)

    return [series[i:i+length] for i in range(0, len(series) - length + 1)]    


def validate_slices(series, slice):
    if slice == 0:
        raise ValueError("slice length cannot be zero")
    if slice < 0:
        raise ValueError("slice length cannot be negative")
    if not series:
        raise ValueError("series cannot be empty")
    if slice > len(series):
        raise ValueError("slice length cannot be greater than series length")