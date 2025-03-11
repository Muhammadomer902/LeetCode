class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = { 'a': 0, 'b': 0, 'c': 0 }
        left = 0
        result = 0
        
        for right in range(len(s)):
            count[s[right]] += 1
            
            while all(count[ch] > 0 for ch in 'abc'):
                count[s[left]] -= 1
                left += 1
            
            # Add the number of valid substrings ending at 'right'
            result += left
        
        return result

        