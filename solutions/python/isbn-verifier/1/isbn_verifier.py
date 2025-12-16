def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
        
    i = 0 
    n = 0
    while i < 9:
        if isbn[i].isdigit():
            n += (10 - i) * int(isbn[i])
        else:
            return False
        i += 1

    if isbn[i].isdigit():
        n += int(isbn[i])
    elif isbn[i] == 'X':
        n += 10
    else:
        return False

    return (n % 11 == 0)
