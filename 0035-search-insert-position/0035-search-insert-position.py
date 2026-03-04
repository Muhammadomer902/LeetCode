class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[len(nums)-1]<target:
            return len(nums)
        if  nums[0]>target:
            return 0
        right = len(nums)-1;left = 0;index = (right+left+1)//2
        while left<=right:
            if nums[index]==target:
                return index
            elif nums[index]<target:
                left = index+1
                index = (right+left+1)//2
            elif nums[index]>target:
                right = index-1
                index = (right+left+1)//2
            
            print(left,right)
        
        return index    