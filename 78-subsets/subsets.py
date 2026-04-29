class Solution:
    def subsets(self, nums):
        result = []
        
        def backtrack(index, path):
            # add current subset
            result.append(path[:])
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        return result