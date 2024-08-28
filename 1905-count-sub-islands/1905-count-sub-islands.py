class Solution:
    def countSubIslands(self, grid1, grid2):
        rows, cols = len(grid1), len(grid1[0])
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid2[r][c] == 0:
                return True
            grid2[r][c] = 0
            is_sub_island = True
            if grid1[r][c] == 0:
                is_sub_island = False
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if not dfs(r + dr, c + dc):
                    is_sub_island = False

            return is_sub_island
    
        sub_island_count = 0
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        sub_island_count += 1

        return sub_island_count
        