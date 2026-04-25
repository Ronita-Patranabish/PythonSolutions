class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)
        
        # Step 1: Ignore leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: Handle sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        # Step 3: Convert digits
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Step 4: Handle overflow
            if result > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31
            
            result = result * 10 + digit
            i += 1
        
        return sign * result
        