class Solution(object):
    def uniqueOccurrences(self, arr):
        from collections import Counter
        
        count = Counter(arr).values()
        return len(count) == len(set(count))
        