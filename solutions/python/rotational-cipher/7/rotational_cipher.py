import string

def rotate(text: str, key: int) -> str:
    letters_map = {string.ascii_letters[idx]: string.ascii_letters[(idx+key)%26] for idx in range(26)}
    letters_map.update({k.upper(): v.upper() for k, v in letters_map.items()})
    return ''.join((letters_map[c] if c.isalpha() else c for c in text))

