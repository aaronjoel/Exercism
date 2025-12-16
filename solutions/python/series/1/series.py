def slices(series, length):
    # get series length
    n = len(series)
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if n == 0:
        raise ValueError("series cannot be empty")
    if length > n:
        raise ValueError("slice length cannot be greater than series length")

    return [series[i:i+length] for i in range(0, n) if len(series[i:i+length]) == length]


        
   
