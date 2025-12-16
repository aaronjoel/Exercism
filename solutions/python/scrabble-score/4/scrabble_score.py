# Keep scores in a dict

LETTER_SCORE = {**dict.fromkeys(list("AEIOULNRST"), 1),
                **dict.fromkeys(list("DG"), 2),
                **dict.fromkeys(list("BCMP"), 3),
                **dict.fromkeys(list("FHVWY"), 4),
                **dict.fromkeys(list("K"), 5),
                **dict.fromkeys(list("JX"), 8),
                **dict.fromkeys(list("QZ"), 10)}



def score(word: str) -> int:
    """Takes an string word and returns it scrabble score according to the
    following rules:
        
        Letter                                  value
        A, E, I, O, U, L, N, R, S, T              1
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

    return sum([LETTER_SCORE.get(ch, 0) for ch in word.upper()])
    