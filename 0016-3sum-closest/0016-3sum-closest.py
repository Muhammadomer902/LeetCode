class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=100000000000
        size = len(nums)
        nums = sorted(nums)
        for i in range(0,size-2):

            if i > 0  and nums[i] == nums[i-1]:
                continue
            
            l,r = i+1,size-1

            while l<r:
                sumt = nums[i] + nums[l] + nums[r]

                if abs(target - sumt) < abs(target - n):
                    n =  sumt 

                if target - sumt < 0:
                    r-=1
                elif target - sumt > 0:
                    l+=1
                else:
                    l+=1
                    
        return n

