class Solution:
    def frequencySort(self, s):
        from collections import Counter
        
        freq = Counter(s)
        
        # sort by (frequency, lexicographically)
        chars = sorted(freq.keys(), key=lambda x: (freq[x], x))
        
        result = []
        for ch in chars:
            result.append(ch * freq[ch])
        
        return "".join(result)