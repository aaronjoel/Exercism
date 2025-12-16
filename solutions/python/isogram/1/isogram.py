def is_isogram(string):
    if string == '':
        return True

    lower_string = string.lower()
    # this could be extended to remove all punctuations marks 
    remove_chars = '- ' 
    lower_string = lower_string.translate(str.maketrans('','', remove_chars))

    unique_chars = set(lower_string)
    char_counts = {}
    for char in lower_string:
        char_counts[char] = char_counts.get(char, 0) + 1

    # If the set has only one element then the string is a isogram
    return len(set(char_counts.values())) == 1

#from collections import Counter

#def is_isogram2(string):
#    if string == '':
#        return True
#    lower_string = ''.join(string.split('-')).lower()
#    char_counts = Counter(string.lower())
#    return set(char_counts.values()) == 1
        
