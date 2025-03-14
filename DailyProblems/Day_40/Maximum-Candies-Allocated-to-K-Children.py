class Solution(object):
    def maximumCandies(self, candies, k):
        if sum(candies) < k:
            return 0
        
        low, high = 1, max(candies)
        result = 0
        
        while low <= high:
            mid = (low + high) // 2
            # Count how many children can be satisfied with `mid` candies
            count = sum(c // mid for c in candies)
            
            if count >= k:
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return result
