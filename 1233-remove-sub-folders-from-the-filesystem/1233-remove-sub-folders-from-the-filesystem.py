class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        # Sort folders lexicographically
        folder.sort()
        
        # Initialize result list with the first folder
        result = [folder[0]]
        
        # Iterate through the sorted folder list starting from the second element
        for i in range(1, len(folder)):
            # Check if current folder is a subfolder of the last folder in result
            # If it's a subfolder, the prefix (result[-1] + '/') should match the start of folder[i]
            if not folder[i].startswith(result[-1] + '/'):
                result.append(folder[i])
        
        return result
