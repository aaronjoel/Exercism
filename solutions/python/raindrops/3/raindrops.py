def convert(number):
    ans = ''
    ans += 'Pling' if number % 3 == 0 else ''
    ans += 'Plang' if number % 5 == 0 else ''
    ans += 'Plong' if number % 7 == 0 else ''
    return ans or str(number)
    

