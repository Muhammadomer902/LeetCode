class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=1
        size =len(nums)
        count = size
        i=1
        while i<size-a:
            if(nums[i-1]==nums[i] and nums[i+1]==nums[i]):
                for j in range(i, size-a):
                    nums[j]=nums[j+1]
                a+=1;count-=1
            else:
                i+=1
        return count