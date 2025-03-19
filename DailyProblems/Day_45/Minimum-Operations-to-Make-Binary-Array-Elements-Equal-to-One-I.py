class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        operations = 0
        
        for i in range(n - 2):
            if nums[i] == 0:
                # We can flip the next three elements
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                operations += 1
        
        # After the loop, check if the last two elements are zeros
        if nums[-2] == 0 or nums[-1] == 0:
            return -1
        
        return operations
