class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        n = len(colors)
        extended_colors = colors + colors[:k - 1]
        count = 0
        invalid_pairs = 0
        
        # Initialize the window (count invalid pairs)
        for i in range(k - 1):
            if extended_colors[i] == extended_colors[i + 1]:
                invalid_pairs += 1
        
        # If there are no invalid pairs, it's a valid alternating group
        if invalid_pairs == 0:
            count += 1
        
        # Slide the window
        for i in range(1, n):
            # Remove outgoing element's effect
            if extended_colors[i - 1] == extended_colors[i]:
                invalid_pairs -= 1
            
            # Add incoming element's effect
            if extended_colors[i + k - 2] == extended_colors[i + k - 1]:
                invalid_pairs += 1
            
            # If no invalid pairs, it's an alternating group
            if invalid_pairs == 0:
                count += 1
        
        return count
