class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        unique1 = set(nums1); unique2=set(nums2);rarr =[]
        for i in unique1:
            if i in unique2:
                rarr.append(i)
        return rarr