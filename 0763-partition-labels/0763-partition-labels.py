class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # Step 1: Store the last occurrence of each character
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        
        # Step 2: Initialize variables
        partitions = []
        start, end = 0, 0
        
        # Step 3: Iterate through the string
        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])
            if i == end:  # When we reach the partition end
                partitions.append(end - start + 1)
                start = i + 1
                
        return partitions
