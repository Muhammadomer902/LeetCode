class Solution(object):
    def moveZeroes(self, nums):
        count=0;size = len(nums)
        for i in range(size):
            if nums[i]!=0:
                nums[count]=nums[i]
                count+=1
        for i in range(count,size):
            nums[i]=0
        return nums