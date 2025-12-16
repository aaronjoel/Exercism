def distance(strand_a, strand_b):
    len_a = len(strand_a)
    len_b = len(strand_b)
    if len_a == 0 and len_b > 0:
        raise ValueError('left empty strand')
    elif len_a > 0 and len_b == 0:
        raise ValueError('right empty strand')
    elif len_a < len_b:
        raise ValueError('second strand longer')
    elif len_a > len_b:
        raise ValueError('first strand longer')
    else:
        return sum([cha != chb for cha, chb in zip(strand_a, strand_b)])
    
    
