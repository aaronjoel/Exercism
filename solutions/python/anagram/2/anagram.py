def find_anagrams(word, candidates):  
    lword = word.lower()
    solutions = [cand for cand in candidates if len(cand) == len(word) and cand.lower() != lword and sorted(list(cand.lower())) == sorted(list(lword))]

    return solutions
    

    
