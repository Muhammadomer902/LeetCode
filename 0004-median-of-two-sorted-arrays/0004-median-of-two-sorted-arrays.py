class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        size1 = len(nums1); size2 = len(nums2)
        i = 0;j = 0;index = 0
        mergedarr = [-1]*(size1+size2)
        while i<size1 or j<size2:
            if i==size1:
                mergedarr[index]=nums2[j]
                j+=1;index+=1
            elif j==size2:
                mergedarr[index]=nums1[i]
                i+=1;index+=1
            elif nums1[i]<=nums2[j]:
                mergedarr[index]=nums1[i]
                i+=1;index+=1
            else:
                mergedarr[index]=nums2[j]
                j+=1;index+=1
        if len(mergedarr)%2==1:
            return mergedarr[int(len(mergedarr)/2)]
        else:
            size = int(len(mergedarr)/2)
            return ((mergedarr[size-1]+mergedarr[size])/2.0)

