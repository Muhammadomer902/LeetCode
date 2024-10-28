class Solution:
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        ans = -1
        for v in nums:
            t = 0
            while v in s:
                v *= v
                t += 1
            if t > 1:
                ans = max(ans, t)
        return ans