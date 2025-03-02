class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        i, j = 0, 0
        merged = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] == nums2[j][0]:  # Common id, sum values
                merged.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:  # nums1 has smaller id
                merged.append(nums1[i])
                i += 1
            else:  # nums2 has smaller id
                merged.append(nums2[j])
                j += 1
        
        # Append remaining elements
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
        
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1
        
        return merged
