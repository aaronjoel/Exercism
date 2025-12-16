import string

LETTERS = string.ascii_letters

def rotate(text:str, key:int) -> str:
    rotated = [LETTERS[(idx+key)%26] for idx in range(26)]
    # Add the upper case letters
    rotated.extend([c.upper() for c in rotated])
    cipher_text = ''.join([rotated[LETTERS.index(c)] if c in LETTERS else c for c in text])
    return cipher_text
