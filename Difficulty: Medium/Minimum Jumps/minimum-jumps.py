class Solution:
    def minJumps(self, arr):
        n = len(arr)
        
        # Edge cases
        if n <= 1:
            return 0
        if arr[0] == 0:
            return -1
        
        jumps = 1
        maxReach = arr[0]
        steps = arr[0]
        
        for i in range(1, n):
            # If we reached last index
            if i == n - 1:
                return jumps
            
            maxReach = max(maxReach, i + arr[i])
            steps -= 1
            
            # No more steps left
            if steps == 0:
                jumps += 1
                
                # Cannot move forward
                if i >= maxReach:
                    return -1
                
                steps = maxReach - i
        
        return -1