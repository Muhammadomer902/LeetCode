class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for c in s:
            if c == '[':
                ans += 1
            elif ans:
                ans -= 1
        return (ans + 1) >> 1
