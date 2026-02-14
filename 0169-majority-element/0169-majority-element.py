class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frq ={};max = -1;maxnum =-1
        for i in nums:
            if i not in frq:
                frq[i] = 1
            else:
                frq[i]+=1
            if frq[i]>max:
                maxnum=i
                max = frq[i]
        return maxnum