class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0:
            return len(s)
            
        n = len(s)
        ans = 0

        for target_unique in range(1, 27):
            left = 0
            count = [0] * 26
            unique = 0
            enough = 0   
            
            for right in range(n):
                idx = ord(s[right]) - ord('a')
                count[idx] += 1
                
                if count[idx] == 1:
                    unique += 1
                if count[idx] == k:
                    enough += 1
                
                while unique > target_unique and left <= right:
                    lidx = ord(s[left]) - ord('a')
                    count[lidx] -= 1
                    if count[lidx] == k - 1:
                        enough -= 1
                    if count[lidx] == 0:
                        unique -= 1
                    left += 1

                if unique == enough:
                    ans = max(ans, right - left + 1)
        
        return ans