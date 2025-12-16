def score(x, y):
    # distance from centre
    d = (x**2 + y**2) ** 0.5
    if d > 10:
        return 0
    elif d > 5 and d <= 10:
        return 1
    elif d > 1 and d <= 5:
        return 5
    else:
        return 10
    
