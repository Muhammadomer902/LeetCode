class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Step 1: Find the dominant element using Boyer-Moore Voting Algorithm
        candidate, count = 0, 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        # Step 2: Count total occurrences of the dominant element
        total_count = nums.count(candidate)
        
        left_count = 0
        n = len(nums)
        
        # Step 3: Try to find the minimum index where the split is valid
        for i in range(n - 1):
            if nums[i] == candidate:
                left_count += 1
            
            left_size = i + 1
            right_size = n - left_size
            
            # Check dominance in both left and right subarrays
            if left_count * 2 > left_size and (total_count - left_count) * 2 > right_size:
                return i
        
        return -1
