class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        total_elements = n * n
        expected_sum = total_elements * (total_elements + 1) // 2
        expected_sq_sum = (total_elements * (total_elements + 1) * (2 * total_elements + 1)) // 6
        
        actual_sum = 0
        actual_sq_sum = 0
        seen = set()
        duplicate = -1
        
        for row in grid:
            for num in row:
                actual_sum += num
                actual_sq_sum += num * num
                if num in seen:
                    duplicate = num
                seen.add(num)
        
        missing = ((expected_sum - actual_sum) + (expected_sq_sum - actual_sq_sum) // (expected_sum - actual_sum)) // 2
        
        return [duplicate, missing]
