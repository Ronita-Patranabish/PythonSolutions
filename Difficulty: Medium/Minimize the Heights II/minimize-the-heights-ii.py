class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()
        
        ans = arr[n-1] - arr[0]
        
        small = arr[0] + k
        big = arr[n-1] - k
        
        if small > big:
            small, big = big, small
        
        for i in range(n-1):
            add = arr[i] + k
            subtract = arr[i+1] - k
            
            if subtract < 0:
                continue
            
            new_min = min(small, subtract)
            new_max = max(big, add)
            
            ans = min(ans, new_max - new_min)
        
        return ans