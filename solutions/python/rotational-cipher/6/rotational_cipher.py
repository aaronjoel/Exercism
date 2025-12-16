import string

LETTERS = string.ascii_letters

def rotate(text:str, key:int) -> str:
    letters_map = {LETTERS[idx] : LETTERS[(idx+key)%26] for idx in range(26)}
    letters_map.update({k.upper() : v.upper() for k, v in letters_map.items()})
    cipher_text = ''.join([letters_map[c] if c.isalpha() else c for c in text])
    return cipher_text
