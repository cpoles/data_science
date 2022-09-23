rna_map = {
    "G": "C",
    "C": "G",
    "T": "A",
    "A": "U"
}


def to_rna(dna_strand):
    return ''.join(map(lambda x: rna_map[x], dna_strand))
