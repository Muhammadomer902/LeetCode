class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        index = {x: i for i, x in enumerate(arr)}  # Store indices of elements
        n = len(arr)
        dp = {}  # Dictionary to store sequence lengths
        max_len = 0
        
        for k in range(n):
            for j in range(k):
                i = index.get(arr[k] - arr[j])  # Check if the Fibonacci condition holds
                if i is not None and i < j:  # Ensure valid indices
                    dp[j, k] = dp.get((i, j), 2) + 1
                    max_len = max(max_len, dp[j, k])
        
        return max_len if max_len >= 3 else 0