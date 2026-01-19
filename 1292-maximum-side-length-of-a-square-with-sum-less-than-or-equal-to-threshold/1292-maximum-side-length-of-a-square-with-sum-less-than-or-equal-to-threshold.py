class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        m, n = len(mat), len(mat[0])

        # Build prefix sum
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre[i][j] = (
                    mat[i-1][j-1]
                    + pre[i-1][j]
                    + pre[i][j-1]
                    - pre[i-1][j-1]
                )

        # Function to check if any k x k square is valid
        def exists_square(k):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    total = (
                        pre[i+k][j+k]
                        - pre[i][j+k]
                        - pre[i+k][j]
                        + pre[i][j]
                    )
                    if total <= threshold:
                        return True
            return False

        # Binary search
        left, right = 0, min(m, n)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if exists_square(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans