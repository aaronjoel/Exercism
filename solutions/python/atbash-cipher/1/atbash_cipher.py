from string import ascii_lowercase as letters
from string import punctuation

CHAR_MAP = {c: r for c, r in zip(letters, letters[::-1])}
PUNCS = punctuation + ' '

def encode(plain_text):
    cipher = [CHAR_MAP.get(c, c) for c in plain_text.lower() if c not in PUNCS]
    cipher_words = [''.join(cipher[i:i+5]) for i in range(0, len(cipher), 5)]
    return ' '.join(cipher_words)

def decode(ciphered_text):
    return ''.join(encode(ciphered_text).split())