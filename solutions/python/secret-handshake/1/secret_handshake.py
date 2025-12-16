def commands(binary_str):
    out_string = []
    e, d, c, b, a = binary_str
    if a == '1':
        out_string.append('wink')
    if b == '1':
        out_string.append('double blink')
    if c == '1':
        out_string.append('close your eyes')
    if d == '1':
        out_string.append('jump')
    if e == '1':
        out_string.reverse()

    return out_string
    
        
