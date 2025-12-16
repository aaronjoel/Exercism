

class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.strip()

    def valid2(self):
        
        # edge cases
        if len(self.card_num) <= 1 or not self.card_num[-1].isdigit():
            return False
        
        # split the string at any white space
        chars = self.card_num.split() 
    
        # deal with non-digits within the sequence
        for char in chars:
            if not char.isdigit():
                return False
        
        digits = [int(i) for i in ''.join(chars)]
       
        
        # double every second digit, starting from the right 
        # subtract 9 if doubling results in a number greater than 9
        double_digits = [2*i if i <= 4 else 2*i - 9 for i in digits[-2::-2]]
       
        
        # perform the sum
        sum_digits = sum(double_digits) + sum(digits[-1::-2])
        
        
        # check validity
        return (sum_digits % 10 == 0)
    
    
    def valid(self):
        
        chars = list(self.card_num)
        
        if len(chars) <= 1 or not chars[-1].isdigit():
            return False
        
        digits = []
        
        for char in chars:
            if char.isdigit():
                digits.append(int(char))
            elif char.isspace():
                continue
            else:
                return False
        
        double_digits = [2*i if i <= 4 else 2*i-9 for i in  digits[-2::-2]]
        
        sum_digits = sum(double_digits) + sum(digits[-1::-2])
        
        return sum_digits % 10 == 0