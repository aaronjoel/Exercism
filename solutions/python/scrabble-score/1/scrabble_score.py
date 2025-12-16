def score(word : str) -> int:
    """Takes an string word and returns it scrabble score according to the
    following rules:
        
        Letter                                  value
        A, E, I, O, U, L, M, R, S, T              1
        D, G                                      2
        B, C, M, P                                3
        F, H, V, W, Y                             4
        K                                         5
        J, X                                      8
        Q, Z                                      10
        
    params
    ------
       word : input str
    
    return
    ------
      score : int, score of the word
    """
    score : int = 0
    u_word = word.upper()
    for ch in u_word:
        if ch in ('A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'):
            score += 1
        if ch in ('D', 'G'):
            score += 2
        if ch in ('B', 'C', 'M', 'P'):
            score += 3
        if ch in ('F', 'H', 'V', 'W', 'Y'):
            score += 4
        if ch == 'K':
            score += 5
        if ch == 'J' or ch == 'X':
            score += 8
        if ch == 'Q' or ch == 'Z':
            score += 10
    
    return score
        

