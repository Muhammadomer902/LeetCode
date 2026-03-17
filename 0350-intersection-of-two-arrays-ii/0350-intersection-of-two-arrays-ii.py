class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num1F = {};rarr =[]
        for i in nums1:
            if i in num1F:
                num1F[i]+=1
            else:
                num1F[i]=1
        for i in nums2:
            if i in num1F and num1F[i]!=0:
                rarr.append(i)
                num1F[i]-=1
        return rarr