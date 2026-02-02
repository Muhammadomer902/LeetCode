class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        start = 0
        min_len = float('inf')

        for end in range(len(nums)):
            sum += nums[end]

            while sum >= target:
                min_len = min(min_len, end - start + 1)
                sum -= nums[start]
                start += 1

        return 0 if min_len == float('inf') else min_len