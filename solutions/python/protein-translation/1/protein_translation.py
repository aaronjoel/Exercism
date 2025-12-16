CODON_TO_PROTEINS = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    'UAA': 'STOP',
    'UAG': 'STOP',
    'UGA': 'STOP'
    
}

def proteins(strand):
    codons = [strand[i:i+3] for i in range(0, len(strand), 3)]
    
    proteine_seq = [CODON_TO_PROTEINS[codon] for codon in codons if codon in CODON_TO_PROTEINS]

    # find position of first 'STOP'
    if 'STOP' in proteine_seq:
        proteine_seq = proteine_seq[:proteine_seq.index('STOP')]
    
    return proteine_seq
