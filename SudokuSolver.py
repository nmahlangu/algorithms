# Write a program to solve a Sudoku puzzle by filling the empty cells.
# Empty cells are indicated by the character '.'.
# You may assume that there will be only one unique solution.

class Solution(object):
    def __init__(self):
        self.valid_entries = [chr(ord('1')+i) for i in xrange(9)]

    def solveSudoku(self, board):
        if not board:
            return -1
        board = [[ch for ch in board[i]] for i in xrange(9)]
        self.solveSudokuHelper(board, 0, 0)
        board = ["".join(board[i]) for i in xrange(9)]
        return board

    def solveSudokuHelper(self, board, row, col):
            # see if done with row
            if col == 9:
                if row == 8:
                    return True
                return self.solveSudokuHelper(board, row + 1, 0)

            # fill current row
            if board[row][col] == '.':
                for i in xrange(1,10):
                    if self.check_and_place(board, row, col, str(i)) and self.solveSudokuHelper(board, row, col + 1):
                        return True
                    board[row][col] = '.'
            elif board[row][col] in self.valid_entries:
                return self.solveSudokuHelper(board, row, col + 1)
            return False

    def check_and_place(self, board, row, col, num):
        for i in xrange(9):
            row_seen = set()
            col_seen = set()
            for j in xrange(9):
                if board[i][j] in row_seen:
                    return False
                elif board[i][j] != '.':
                    row_seen.add(board[i][j])

                if board[j][i] in col_seen:
                    return False
                elif board[j][i] != '.':
                    col_seen.add(board[j][i])

        for i in xrange(0, 9, 3):
            for j in xrange(0, 9, 3):
                block = set()
                for ii in xrange(i,i+3):
                    for jj in xrange(j,j+3):
                        if board[ii][jj] in block:
                            return False
                        elif board[ii][jj] != '.':
                            block.add(board[ii][jj])


        board[row][col] = num
        return True

# Solution: A good solution to this problem is backtracking. Add a number an open
# spot in the board and check if the board is still valid. If it is, keep going;
# if it's not, remove the number that was just added and add the next highest, repeating
# the aforementioned check. If you try every number and none work, go back up one level
# in the recursion and add the next number possible at the previous space. Repeat
# until a solution is found. Time complexity is O(9^m), where m is the number of blank
# spaces and 9 is the number of possiblities for each blank, and space complexity is O(1).
