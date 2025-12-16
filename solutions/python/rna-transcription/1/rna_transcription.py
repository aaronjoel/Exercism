def to_rna(dna_strand):
    transcription = {'G' : 'C',
                     'C' : 'G',
                     'T' : 'A',
                     'A' : 'U'}
    rna_strand = ""
    for nucleotide in dna_strand:
        rna_strand += transcription.get(nucleotide, nucleotide)
    return rna_strand
