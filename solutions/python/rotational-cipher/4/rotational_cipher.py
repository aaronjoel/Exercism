import string

LETTERS = string.ascii_lowercase

def rotate(text:str, key:int) -> str:
    letters_map = {LETTERS[idx] : LETTERS[(idx+key)%26] for idx in range(26)}
    
    cipher_text = []
    for c in text:
        if c.islower():
            cipher_text.append(letters_map[c]) 
        elif c.isupper():
            cipher_text.append(letters_map[c.lower()].upper())
        else:
            cipher_text.append(c)
    return ''.join(cipher_text)
