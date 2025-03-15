class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right = min(nums), max(nums)
        
        def can_rob_with_capability(cap):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= cap:
                    count += 1
                    i += 1  # Skip the next adjacent house
                i += 1
            return count >= k
        
        while left < right:
            mid = (left + right) // 2
            if can_rob_with_capability(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
