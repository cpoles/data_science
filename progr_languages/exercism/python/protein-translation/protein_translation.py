CODONS_PROTEIN = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP"

}

import re

def proteins(strand):
    sequence = []
    codons = re.findall(r'[ACUG]{3}', strand)
    for codon in codons:
        if CODONS_PROTEIN[codon] == 'STOP':
            break
        sequence.append(CODONS_PROTEIN[codon])
    return sequence
