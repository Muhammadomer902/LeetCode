class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        current_and = 0
        max_len = 0
        
        for right in range(len(nums)):
            # If AND condition breaks, shrink the window from left
            while (current_and & nums[right]) != 0:
                current_and ^= nums[left]
                left += 1
            
            # Include nums[right] in the window
            current_and |= nums[right]
            max_len = max(max_len, right - left + 1)
        
        return max_len
