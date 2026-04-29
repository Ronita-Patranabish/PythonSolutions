class Solution:
    
    def firstOne(self, row):
        left, right = 0, len(row) - 1
        ans = len(row)
        
        while left <= right:
            mid = (left + right) // 2
            
            if row[mid] == 1:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
    
    def rowWithMax1s(self, arr):
        n = len(arr)
        m = len(arr[0])
        
        max_count = 0
        result = -1
        
        for i in range(n):
            first = self.firstOne(arr[i])
            
            # if no 1 in row
            if first == m:
                continue
            
            count = m - first
            
            if count > max_count:
                max_count = count
                result = i
        
        return result