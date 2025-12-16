def sum_of_multiples(limit, multiples):
    return sum(set([m*i for m in [e for e in multiples if e != 0] for i in range(1, 1+limit//m) if m*i < limit]))
    
