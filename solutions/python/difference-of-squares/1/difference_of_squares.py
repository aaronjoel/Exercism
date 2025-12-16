def square_of_sum(number):
    n_sum = (number * (number + 1)) // 2
    return n_sum * n_sum


def sum_of_squares(number):
    n_sq_sum = number * (number + 1) * (2*number + 1) // 6
    return n_sq_sum


def difference_of_squares(number):
    sq_of_sum = square_of_sum(number)
    sum_of_sq = sum_of_squares(number)
    return sq_of_sum - sum_of_sq
