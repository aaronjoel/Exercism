NOUNS_AND_VERBS = [
    ("house that Jack built.", "lay in"),
    ("malt", "ate"),
    ("rat", "killed"),
    ("cat", "worried"),
    ("dog", "tossed"),
    ("cow with the crumpled horn", "milked"),
    ("maiden all forlorn", "kissed"),
    ("man all tattered and torn", "married"),
    ("priest all shaven and shorn", "woke"),
    ("rooster that crowed in the morn", "kept"),
    ("farmer sowing his corn", "belonged to"),
    ("horse and the hound and the horn", "")
]

def get_verse(n: int) -> str:
    """
    Return the nth verse in the rhyme.
    """
    noun = NOUNS_AND_VERBS[n-1][0]
    result = [f"This is the {noun}"]
    for noun, verb in reversed(NOUNS_AND_VERBS[:n-1]):
        result.append(f"that {verb} the {noun}")
    return " ".join(result)

def recite(start_verse:int, end_verse:int) -> str:
    """
    Recite the rhyme.
    """
    results = [get_verse(n) for n in range(start_verse, end_verse+1)]
    return results
