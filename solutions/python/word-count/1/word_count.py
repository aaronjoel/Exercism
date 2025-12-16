def count_words(sentence):
    """
    Counts the occurrences of each word in sentence.
    The count is case insensitive.
    
    params
    ------
       sentence: a str whose words are counted
    
    returns
    -------
       A dict with words as keys and counts as values
    """
    
    import re
    from string import punctuation
    
    # lower the characters, replace underscores with spaces and use find all words
    words = [word.strip(punctuation) for word in re.findall(r"[\w']+", sentence.lower().replace('_', ' '))]
    
    word_count = {}
    
    for word in set(words):
        word_count[word] = words.count(word)
    
    return word_count

def count_words_2(sentence):

    
    from string import punctuation
    from collections import Counter
    from re import findall
    
    words = [word.strip(punctuation) for word in findall(r"[\w']+", sentence.lower().replace('_', ' '))]
    word_counter = dict(Counter(words))
    
    return word_counter
