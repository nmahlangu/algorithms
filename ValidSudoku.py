# Determine if a Sudoku board is valid.
# The Sudoku board could be partially filled, where empty cells are
# filled with the character '.'

from sets import Set

class Solution(object):
    def __init__(self):
        self.width = self.height = 9

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check rows and columns
        for i in xrange(self.height):
            row = set()
            col = set()
            for j in xrange(self.width):
                # row
                if board[i][j] in row:
                    return False
                elif board[i][j] != '.':
                    row.add(board[i][j])
        
                # col
                if board[j][i] in col:
                    return False
                elif board[j][i] != '.':
                    col.add(board[j][i])

        # check blocks
        for i in xrange(0, self.height, 3):
            for j in xrange(0, self.width, 3):
                block = set()
                for ii in xrange(i,i+3):
                    for jj in xrange(j,j+3):
                        if board[ii][jj] in block:
                            return False
                        elif board[ii][jj] != '.':
                            block.add(board[ii][jj])
        return True

# Solution: Iterate through the board with 2 nested for loops (one can cleverly
# check rows and columns simultaneously). If there's any duplicates in a row
# or columns, return False. To check each block, start from the top left and
# check each row of blocks to see if they're valid. Time complexity is
# O(n) and space complexity is O(1).

