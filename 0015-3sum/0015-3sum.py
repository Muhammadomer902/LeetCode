class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        x = []
        seen = set()
        index = 0;
        if len(nums)<3:
            return []
        nums = sorted(nums)
        print(nums)
        for i in range(0,len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k]==0:
                        t = tuple([nums[i],nums[j],nums[k]])
                        if t not in seen:
                            seen.add(t)
                            x.append(t)
        return x