def equilateral(sides):
    a, b, c = sides
    cond_0 = all([side > 0 for side in sides])
    cond_1 = (a + b >= c) and (b + c >= a) and (a + c >= b)
    cond_2 = (a == b and b == c)
    return (cond_0 and cond_1 and cond_2)

def isosceles(sides):
    a, b, c = sides
    cond_0 = all([side > 0 for side in sides])
    cond_1 = (a + b >= c) and (b + c >= a) and (a + c >= b)
    cond_2 = (a == b or a == c or b == c)
    return (cond_0 and cond_1 and cond_2)


def scalene(sides):
    a, b, c = sides
    cond_0 = all([side > 0 for side in sides])
    cond_1 = (a + b >= c) and (b + c >= a) and (a + c >= b)
    cond_2 = (a != b and b != c and a != c)
    return (cond_0 and cond_1 and cond_2)
