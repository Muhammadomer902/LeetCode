class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        # Initial count of 'W' in the first window of size k
        min_ops = blocks[:k].count('W')
        curr_ops = min_ops
        
        for i in range(k, len(blocks)):
            # Remove the leftmost element from the window
            if blocks[i - k] == 'W':
                curr_ops -= 1
            # Add the new element to the window
            if blocks[i] == 'W':
                curr_ops += 1
            # Update the minimum operations required
            min_ops = min(min_ops, curr_ops)
        
        return min_ops
