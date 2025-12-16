def value(colors):
    color_to_val = {'black' : 0,
                    'brown' : 1,
                    'red' : 2,
                    'orange' : 3,
                    'yellow' : 4,
                    'green' : 5,
                    'blue' : 6,
                    'violet' : 7,
                    'grey' : 8,
                    'white' : 9}

    _colors = [col.lower() for col in colors][:2]
    resistance = 0
    for i, color in enumerate(_colors):
        resistance += 10**(1-i) * color_to_val.get(color)

    return resistance
