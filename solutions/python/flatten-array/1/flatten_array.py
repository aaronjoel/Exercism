def flatten(iterable):
    flat_list = []
    for item in iterable:
        if type(item) == list:
            flat_list += flatten(item)
        elif type(item) == type(None):
            continue
        else:
            flat_list.append(item)
    return flat_list
