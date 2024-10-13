import heapq

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        # Initialize the heap
        min_heap = []
        current_max = float('-inf')
        
        # Insert the first element of each list along with the row and column index
        for row in range(len(nums)):
            heapq.heappush(min_heap, (nums[row][0], row, 0))
            current_max = max(current_max, nums[row][0])
        
        # Initialize the smallest range
        smallest_range = [-float('inf'), float('inf')]
        
        while min_heap:
            # Get the smallest element from the heap
            current_min, row, col = heapq.heappop(min_heap)
            
            # Check if the current range is smaller
            if current_max - current_min < smallest_range[1] - smallest_range[0]:
                smallest_range = [current_min, current_max]
            
            # If we have exhausted the current list, break
            if col + 1 == len(nums[row]):
                break
            
            # Get the next element from the same list
            next_val = nums[row][col + 1]
            heapq.heappush(min_heap, (next_val, row, col + 1))
            
            # Update the current max
            current_max = max(current_max, next_val)
        
        return smallest_range
