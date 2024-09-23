class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        # Create a set of words for O(1) lookup
        word_set = set(dictionary)
        n = len(s)
        
        # DP array to store the minimum number of extra characters for each position
        dp = [0] * (n + 1)
        
        # Iterate through each index in the string `s`
        for i in range(1, n + 1):
            # Initialize dp[i] as dp[i-1] + 1 (consider current character as extra)
            dp[i] = dp[i - 1] + 1
            
            # Try to match every substring ending at index i-1
            for j in range(i):
                if s[j:i] in word_set:
                    dp[i] = min(dp[i], dp[j])
        
        # The last element in dp array holds the result
        return dp[n]