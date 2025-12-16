import re

def abbreviate(words: str) -> str:
    # split the string at ',', '_' or '-' and keep the first char of each word
    return "".join(word[0] for word in re.split(r'[\s,_-]+', words)).upper()

