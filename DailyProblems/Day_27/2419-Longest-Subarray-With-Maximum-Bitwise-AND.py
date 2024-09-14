class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums);count=0;max_count=0;
        for i in nums:
            if i ==max_num:
                count+=1
                max_count = max(max_count, count)
            elif count>0 and i!=max_num:
                count=0
        return max_count