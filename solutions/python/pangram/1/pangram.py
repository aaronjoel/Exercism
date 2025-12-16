import re

def is_pangram(sentence):
    processed = re.sub(r'[(^\W)\s]', '', sentence).lower()
    chars_set = set(processed)
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
    return len(alphabet_set - chars_set) == 0
    
    