def convert(number):
    ans = ''
    if number % 3 == 0:
        ans += 'Pling'
    if number % 5 == 0:
        ans += 'Plang'
    if number % 7 == 0:
        ans += 'Plong'
    if ans == '':
        ans = str(number)
    return ans
