class Solution:
    def combinationSum(self, n, k):   # <-- FIXED ORDER
        res = []
        
        def backtrack(start, k, target, path):
            if k == 0 and target == 0:
                res.append(path[:])
                return
            
            if k == 0 or target < 0:
                return
            
            for num in range(start, 10):
                if num > target:
                    break
                
                path.append(num)
                backtrack(num + 1, k - 1, target - num, path)
                path.pop()
        
        backtrack(1, k, n, [])
        return res