class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def countNegatives(nums):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < 0:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        def countPositives(nums):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= 0:
                    left = mid + 1
                else:
                    right = mid - 1
            return len(nums) - left
        
        neg_count = countNegatives(nums)
        pos_count = countPositives(nums)
        
        return max(neg_count, pos_count)
