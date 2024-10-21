class Solution(object):
    def maxUniqueSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Backtracking function
        def backtrack(start, seen):
            # If we've reached the end of the string, return 0
            if start == len(s):
                return 0
            
            max_count = 0
            
            # Try all possible substrings starting from index `start`
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                
                # If the substring is not seen, proceed with it
                if substring not in seen:
                    seen.add(substring)
                    # Recursively backtrack for the remaining part of the string
                    count = 1 + backtrack(end, seen)
                    max_count = max(max_count, count)
                    seen.remove(substring)  
            
            return max_count
        return backtrack(0, set())
