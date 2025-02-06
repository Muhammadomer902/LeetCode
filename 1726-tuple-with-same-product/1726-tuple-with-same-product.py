from collections import defaultdict

class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product_count = defaultdict(int)
        n = len(nums)
        
        # Count occurrences of each product from pairs (a, b)
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1
        
        result = 0
        
        # For each product that appears at least twice, compute valid tuples
        for count in product_count.values():
            if count > 1:
                result += (count * (count - 1)) // 2 * 8
                
        return result