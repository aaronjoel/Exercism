def rotate(text, key):
    import string
    if key == 26 or key == 0:
        return text
        
    lower_letters_map = {i : c for i, c in enumerate(string.ascii_lowercase)}
    cipher_text = []
    val_a = ord('a')
    for c in text:
        if c.islower():
            idx = (ord(c) - val_a + key) % 26
            cipher_text.append(lower_letters_map[idx])
        elif c.isupper():
            idx = (ord(c.lower()) - val_a + key) % 26
            cipher_text.append(lower_letters_map[idx].upper())
        else:
            cipher_text.append(c)
    return ''.join(cipher_text)
