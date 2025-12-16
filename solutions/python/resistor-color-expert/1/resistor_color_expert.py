COLORS_TO_VALS = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

COLS_TOLS = {
    'grey': 0.05,
    'violet': 0.1,
    'blue': 0.25,
    'green': 0.5,
    'brown': 1,
    'red': 2,
    'gold': 5,
    'silver': 10
}

def resistor_label(colors):
    N = len(colors)
    if N == 1:
        return f'{COLORS_TO_VALS[colors[0]]} ohms'
    elif N == 4:
        resistance = (10*COLORS_TO_VALS[colors[0]] + COLORS_TO_VALS[colors[1]]) * 10**COLORS_TO_VALS[colors[2]]
        tol = COLS_TOLS.get(colors[3], 0)
    else:
        resistance = (100*COLORS_TO_VALS[colors[0]] + 10*COLORS_TO_VALS[colors[1]] + COLORS_TO_VALS[colors[2]]) * 10**COLORS_TO_VALS[colors[3]]
        tol = COLS_TOLS.get(colors[4], 0)

    if resistance >= 1_000_000_000:
        resistance = f'{resistance/1_000_000_000} gigaohms'
    elif resistance >= 1_000_000:
        resistance = f'{resistance/1_000_000} megaohms'
    elif resistance >= 1_000:
        if resistance % 1000 == 0:
            resistance = f'{int(resistance/1_000)} kiloohms'
        else:
            resistance = f'{resistance/1_000} kiloohms'
    else:
        resistance = f'{resistance} ohms'

    if tol > 0:
        return f'{resistance} ±{tol}%'
    return resistance
        



    
        
    
    
