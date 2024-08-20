class Solution {
public:
    int stoneGameII(vector<int>& piles) {
        int n = piles.size();
        
        vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));
        vector<int> suffix_sum(n + 1, 0);
        
        for (int i = n - 1; i >= 0; --i) {
            suffix_sum[i] = suffix_sum[i + 1] + piles[i];
        }
        
        function<int(int, int)> helper = [&](int i, int m) {
            if (i == n) {
                return 0;
            }
            if (dp[i][m] != 0) {
                return dp[i][m];
            }
            
            int max_stones = 0;
            for (int x = 1; x <= 2 * m; ++x) {
                if (i + x <= n) {
                    max_stones = max(max_stones, suffix_sum[i] - helper(i + x, max(m, x)));
                }
            }
            
            dp[i][m] = max_stones;
            return dp[i][m];
        };
        
        return helper(0, 1);
    }
};