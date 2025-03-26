class Solution(object):
    def minOperations(self, grid, x):
        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        # Step 1: Flatten the grid into a 1D array
        arr = [num for row in grid for num in row]
        
        # Step 2: Check if transformation is possible
        remainder = arr[0] % x
        for num in arr:
            if num % x != remainder:
                return -1
        
        # Step 3: Find the median
        arr.sort()
        median = arr[len(arr) // 2]
        
        # Step 4: Calculate minimum operations to make all elements equal to median
        operations = sum(abs(num - median) // x for num in arr)
        
        return operations
