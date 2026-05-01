class Solution:
    def minMen(self, arr):
        n = len(arr)
        intervals = []
        
        # Step 1: Build intervals
        for i in range(n):
            if arr[i] != -1:
                left = max(0, i - arr[i])
                right = min(n - 1, i + arr[i])
                intervals.append((left, right))
        
        # Step 2: Sort intervals
        intervals.sort()
        
        count = 0
        i = 0
        current_end = -1
        farthest = -1
        
        # Step 3: Greedy coverage
        while current_end < n - 1:
            while i < len(intervals) and intervals[i][0] <= current_end + 1:
                farthest = max(farthest, intervals[i][1])
                i += 1
            
            # If cannot extend coverage → gap
            if farthest <= current_end:
                return -1
            
            current_end = farthest
            count += 1
        
        return count