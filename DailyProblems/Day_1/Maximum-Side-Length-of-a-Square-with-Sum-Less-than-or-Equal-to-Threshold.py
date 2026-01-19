1class Solution(object):
2    def maxSideLength(self, mat, threshold):
3        """
4        :type mat: List[List[int]]
5        :type threshold: int
6        :rtype: int
7        """
8        m, n = len(mat), len(mat[0])
9
10        # Build prefix sum
11        pre = [[0] * (n + 1) for _ in range(m + 1)]
12        for i in range(1, m + 1):
13            for j in range(1, n + 1):
14                pre[i][j] = (
15                    mat[i-1][j-1]
16                    + pre[i-1][j]
17                    + pre[i][j-1]
18                    - pre[i-1][j-1]
19                )
20
21        # Function to check if any k x k square is valid
22        def exists_square(k):
23            for i in range(m - k + 1):
24                for j in range(n - k + 1):
25                    total = (
26                        pre[i+k][j+k]
27                        - pre[i][j+k]
28                        - pre[i+k][j]
29                        + pre[i][j]
30                    )
31                    if total <= threshold:
32                        return True
33            return False
34
35        # Binary search
36        left, right = 0, min(m, n)
37        ans = 0
38
39        while left <= right:
40            mid = (left + right) // 2
41            if exists_square(mid):
42                ans = mid
43                left = mid + 1
44            else:
45                right = mid - 1
46
47        return ans