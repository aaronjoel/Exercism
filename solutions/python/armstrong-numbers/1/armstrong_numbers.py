def is_armstrong_number(number):
    if number % 10 == number:
        return True

    num = number
    digits = []
    num_digits = 0
    while num > 0:
        digits.append(num % 10)
        num = num // 10
        num_digits += 1
    armstrong_sum = sum([digit**num_digits for digit in digits])
    return (armstrong_sum == number)
        
