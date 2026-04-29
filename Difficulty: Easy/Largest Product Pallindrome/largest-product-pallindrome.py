class Solution:
    
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
    
    def LargestProductPalin(self, N):
        max_num = 10**N - 1
        min_num = 10**(N - 1)
        
        result = 0
        
        for i in range(max_num, min_num - 1, -1):
            for j in range(i, min_num - 1, -1):
                product = i * j
                
                if product <= result:
                    break
                
                if self.isPalindrome(product):
                    result = product
        
        return result