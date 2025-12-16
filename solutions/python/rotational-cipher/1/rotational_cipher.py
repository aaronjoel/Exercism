def rotate(text, key):
    if key == 26 or key == 0:
        return text

    lower_alphabets = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_letters_map = {i : c for i, c in enumerate(lower_alphabets)}
    upper_letters_map = {i : c for i, c in enumerate(upper_alphabets)}
    cipher_text = ''
    for c in text:
        if c.islower():
            idx = (ord(c) - ord('a') + key) % 26
            cipher_text += lower_letters_map[idx]
        elif c.isupper():
            idx = (ord(c) - ord('A') + key) % 26
            cipher_text += upper_letters_map[idx]
        else:
            cipher_text += c
    return cipher_text
