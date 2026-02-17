class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numChecked = {}
        for i, num in enumerate(nums):
            remainder = target - num

            if remainder in numChecked:
                return [numChecked[remainder], i]
            
            numChecked[num] = i