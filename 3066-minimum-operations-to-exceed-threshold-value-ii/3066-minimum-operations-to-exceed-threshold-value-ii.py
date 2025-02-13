import heapq

class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        operations = 0
        
        while nums[0] < k:
            if len(nums) < 2:
                return -1  
            
            x = heapq.heappop(nums)  
            y = heapq.heappop(nums) 
            
            new_element = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, new_element)
            
            operations += 1
        
        return operations