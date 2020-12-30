# 36. Valid Sudoku
class Solution:
    def isValidSudoku(self, board):
        # row check
        for i in range(len(board)):
            rowVals = []
            for j in range(len(board[0])):
                # print(i, j, board[i][j], rowVals)
                if board[i][j]==".":
                    continue
                elif(0 < int(board[i][j]) < 10) and \
                    (board[i][j] not in rowVals):
                    rowVals.append(board[i][j])
                else:
                    return False
        # column check
        for i in range(len(board)):
            colVals = []
            for j in range(len(board[0])):
                if board[j][i]==".":
                    continue
                elif(0 < int(board[j][i]) < 10):
                    colVals.append(board[j][i])
            if len(set(colVals)) < len(colVals):
                return False
        # sub-boxes check
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subBoxVals = board[i][j:j+3] + \
                    board[i+1][j:j+3] + board[i+2][j:j+3]
                tempVals = []
                for val in subBoxVals:
                    if val==".":
                        continue
                    elif(0 < int(val) < 10) and \
                        (val not in tempVals):
                        tempVals.append(val)
                    else:
                        return False
                        
        return True

# Test
solution = Solution()
# Expected: True
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(solution.isValidSudoku(board))
# Expected: False
board2 = [
    [".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]
]
print(solution.isValidSudoku(board2))

foo = [[1,2,3],[1,6,7]]
print(zip(*[[1, 2, 3], [5,6,7]]))
print([i for i in zip(*[[1, 2, 3], [5,6,7]])])

import collections
collections.Counter(x for i, row in enumerate(foo) for j, c in enumerate(row) if c != '.' for x in ((c, i), (j, c), (i/3, j/3, c))).values()

len([x for i, row in enumerate(foo) 
                for j, c in enumerate(row) 
                    if c!='.' for x in ((c,i),(j,c),(i/3,j/3,c))])
