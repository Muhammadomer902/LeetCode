class Solution(object):
    # def iterateRow(self, board, row, num):

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(0,9):
            seenSetR = set();seenSetC = set()
            for j in range(0,9):
                if board[i][j]!="." and board[i][j] in seenSetR:
                    return False
                elif board[i][j]!="." and board[i][j] not in seenSetR:
                    seenSetR.add(board[i][j])
            for j in range(0,9):
                if board[j][i]!="." and board[j][i] in seenSetC:
                    return False
                elif board[j][i]!="." and board[j][i] not in seenSetC:
                    seenSetC.add(board[j][i])

        for boxRow in range(0,9,3):
            for boxCol in range(0,9,3):
                seen = set()

                for i in range(3):
                    for j in range(3):
                        val = board[boxRow+i][boxCol+j]
                        if val != ".":
                            if val in seen:
                                return False
                            seen.add(val)
        return True