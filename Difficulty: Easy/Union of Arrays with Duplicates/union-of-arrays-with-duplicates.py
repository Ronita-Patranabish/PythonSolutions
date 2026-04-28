class Solution:
    def findUnion(self, a, b):
        # Use set to store unique elements
        s = set()
        
        # Add elements from both arrays
        for num in a:
            s.add(num)
        for num in b:
            s.add(num)
        
        # Return as list
        return list(s)