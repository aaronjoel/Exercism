def rows(letter):
    ch = letter.upper()
    A = 'A'
    ord_A = ord(A)
    n = ord(ch) - ord_A
    sym = ' '
    if n == 0:
        return [A]
    # first row
    out = n*sym + A + n*sym + '\n' 
    # in-between rows
    for i in range(n-1):
        c = chr(ord_A + i + 1)
        right = (n-i-1)*sym + c + i*sym  
        left = i*sym + c + (n-i-1)*sym 
        out += right + sym + left + '\n'
    # middle row
    if n > 0:
        middle = ch + (2*n-1)*sym + ch 
        out = out + middle + out[::-1]
    return out.split('\n')
