class Solution:
    def hasTripletSum(self, arr, target):   # ✅ correct name
        n = len(arr)
        arr.sort()
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                s = arr[i] + arr[left] + arr[right]
                
                if s == target:
                    return True
                elif s < target:
                    left += 1
                else:
                    right -= 1
        
        return False