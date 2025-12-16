def append(list1, list2):
    return list1 + list2


def concat(lists):
    m = length(lists)
    if m == 0:
        return lists
    elif m == 1:
        return lists[0]
    else:
        list0 = lists[0]
        for _list in lists[1:]:
            for item in _list:
                list0 += [item]
        return list0


def filter(function, list):
    return [e for e in list if function(e)]


def length(list):
    _sum = 0
    for e in list:
        _sum += 1
    return _sum


def map(function, list):
    return [function(e) for e in list]


def foldl(function, list, initial):
    if length(list) == 0:
        return initial

    if isinstance(list[0], str):
        res = ''
        for e in list:
            res = e + res
        res = initial + res
        return res
    else:
        for e in list:
            initial = function(initial, e)
        return initial


def foldr(function, list, initial):
    if length(list) == 0:
        return initial
        
    if isinstance(list[0], str):
        res = ''
        for e in list:
            res = res + e
        res = res + initial
        return res
    else:
        for e in list:
            initial = function(e, initial)
        return initial


def reverse(list):
    n = length(list)
    m = n // 2
    for i in range(m):
        list[i], list[n-i-1] = list[n-i-1], list[i]
    return list
    
