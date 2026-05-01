class Solution:
    def countLessEqual(self, arr, x):
        n = len(arr)
        
        # Step 1: Find pivot (smallest element)
        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid
        pivot = low
        
        # Helper: count elements <= x in sorted subarray
        def count(arr, l, r, x):
            low, high = l, r
            ans = l - 1
            
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] <= x:
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1
            
            return ans - l + 1
        
        # Step 2: count in both parts
        count1 = count(arr, pivot, n - 1, x)
        count2 = count(arr, 0, pivot - 1, x)
        
        return count1 + count2