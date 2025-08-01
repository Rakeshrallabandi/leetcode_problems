class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            k = {}
            for j in i:
                if j in k and j != '.':
                    return False
                k[j] = 1
        for i in range(9):
            k = {}
            for j in range(9):
                if board[j][i] in k and board[j][i] != '.':
                    return False
                k[board[j][i]] = 1
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                k = {}
                for i in range(3):
                    for j in range(3):
                        val = board[row + i][col + j]
                        if val in k and val != '.':
                            return False
                        k[val] = 1
        return True
