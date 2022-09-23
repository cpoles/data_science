def distance(strand_a, strand_b):
    if not len(strand_a) == len(strand_b):
        raise ValueError("Strands must be of equal length.")

    return sum([a != b for a, b in zip(strand_a, strand_b)])
    
