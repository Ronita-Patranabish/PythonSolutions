class Solution:
    
    def countLessEqual(self, row, target):
        # count elements <= target using binary search
        left, right = 0, len(row)
        
        while left < right:
            mid = (left + right) // 2
            
            if row[mid] <= target:
                left = mid + 1
            else:
                right = mid
        
        return left
    
    def median(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        low = float('inf')
        high = float('-inf')
        
        # find range
        for i in range(n):
            low = min(low, mat[i][0])
            high = max(high, mat[i][m - 1])
        
        desired = (n * m) // 2 + 1
        
        # binary search on answer
        while low <= high:
            mid = (low + high) // 2
            
            count = 0
            for i in range(n):
                count += self.countLessEqual(mat[i], mid)
            
            if count < desired:
                low = mid + 1
            else:
                high = mid - 1
        
        return low