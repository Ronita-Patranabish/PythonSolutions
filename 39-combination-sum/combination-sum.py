class Solution:
    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()
        
        def backtrack(start, current, remaining):
            # base case
            if remaining == 0:
                result.append(current[:])
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                
                # choose
                current.append(candidates[i])
                
                # stay on same index (reuse allowed)
                backtrack(i, current, remaining - candidates[i])
                
                # backtrack
                current.pop()
        
        backtrack(0, [], target)
        return result