# Keep scores in a dict

LETTER_SCORE = {
    "A": 1,
    "E": 1,
    "I": 1,
    "L": 1,
    "N": 1,
    "O": 1,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 1,
    "D": 2,
    "G": 2,
    "B": 3,
    "C": 3,
    "M": 3,
    "P": 3,
    "F": 4,
    "H": 4,
    "V": 4,
    "W": 4,
    "Y": 4,
    "K": 5,
    "J": 8,
    "X": 8,
    "Q": 10,
    "Z": 10,
}


def score(word: str) -> int:
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

    return sum([LETTER_SCORE.get(ch, 0) for ch in word.upper()])
    