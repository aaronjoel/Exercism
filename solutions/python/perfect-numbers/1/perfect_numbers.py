def _factors(number):
    """ Return the list of factors of a number.
    
    :param number: int a positive integer
    :return: list the list of factors of the input integer
    """
    import math
    list_of_factors = [1] if number > 1 else []
    n = math.ceil(number ** 0.5)
    for d in range(2, n+1):
        if d == number:
            break
        q, r = number // d, number % d
        if r == 0:
            if d not in list_of_factors:
                list_of_factors.append(d)
            if q not in list_of_factors:
                list_of_factors.append(q)
    return list_of_factors

def aliquot_sum(number):
    return sum(_factors(number))

def perfect(number):
    return aliquot_sum(number) == number

def abundant(number):
    return number < aliquot_sum(number)

def deficient(number):
    return number > aliquot_sum(number)

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0 or not isinstance(number, int):
        raise ValueError("Classification is only possible for positive integers.")
    if perfect(number):
        return "perfect"
    elif abundant(number):
        return "abundant"
    else:
        return "deficient"
