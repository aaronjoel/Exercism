def label(colors):
    color_mapping = {'black' : 0,
                     'brown' : 1,
                     'red' : 2,
                     'orange' : 3,
                     'yellow' : 4,
                     'green' : 5,
                     'blue' : 6,
                     'violet' : 7,
                     'grey' : 8,
                     'white' : 9}

    colors = [color.lower() for color in colors][:3]  # Ensure we are dealing with 3 colors
    resistance = 10*color_mapping[colors[0]] + color_mapping[colors[1]]
    # dealing with the 3rd colors
    num_zeros = 10**color_mapping[colors[-1]]
    resistance *= num_zeros

    giga = int(resistance // 1e9)
    mega = int(resistance // 1e6)
    kilo = int(resistance // 1e3)

    if giga > 0:
        return f"{giga} gigaohms"
    elif mega > 0:
        return f"{mega} megaohms"
    elif kilo > 0:
        return f"{kilo} kiloohms"
    else:
        return f"{resistance} ohms"
    
