class Solution:
    def countSquares(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        total_squares = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1 and i > 0 and j > 0:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                total_squares += matrix[i][j]
        
        return total_squares
