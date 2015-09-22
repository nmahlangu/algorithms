# Given an integer n, determine if there is some arrangement of n queens
# on an n-by-n chessboard such that no queens attack another queen

def n_queens(n):
    board = [0 for i in xrange(n)]
    return n_queens_helper(board, n, 0)

def n_queens_helper(board, n, queens):
    # base case
    if queens == n:
        return True
    
    # recursive case - try to place queen in a column
    for i in xrange(n):
        if check_and_place(board, queens, i) and n_queens_helper(board, n, queens + 1):
            return True
    return False

def check_and_place(board, row, col):
    for i in xrange(row):
        # check previous rows' columns + diagonals
        if board[i] == col or (row - i == abs(col - board[i])):
            return False

    board[row] = col
    return True

# Solution: The solution above implements backtracking. Build up a one dimensional 
# array storing valid places for the arrangement of queens: index represents the row 
# and the value at an index represents a column. Recursively iterate through the
# rows and do the following. For each column in the current row, if the queen 
# can safely be inserted, do so and move on. If it can't be placed into any column,
# go back up a level in the recursive and try to place the previous queen elsewhere.
# If all n queens can be placed, return True. Time complexity is O(n!) - initially,
# there are n^2Cn permutations of the queens. Using the constraint that each queen
# must be in its own row reduces the number of permutations to O(n^n). Furthermore,
# using the constraint that each queen must also be in its own column reduces the number
# of permutations to O(n!). Space complexity is O(n).
