class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        col = [];n = len(grid[0]);count =0
        for i in range(n):
            c =[]
            for j in range(n):
                c.append(grid[j][i])
            col.append(c)
        for i in grid:
            for j in col:
                if i==j:
                    count+=1
        return count