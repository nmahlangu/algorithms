# Imagine a robobt sitting on the upper left corner of a grid with r rows
# and c columns. The robot can only move in two directions, right and down,
# but certain cells are "off limits" such that the robot cannot step on
# them. Design an algorithm to find a path for the robot from the top left
# to the bottom right. 

cache = {}

def get_path(matrix):
    if not matrix:
        return None
    path = []
    if helper(matrix,len(matrix)-1,len(matrix[0])-1,path):
        return path
    return None

def helper(matrix,i,j,path):
    # check for memoization:
    if (i,j) in cache:
        return cache[(i,j)]

    # base case
    if i < 0 or j < 0 or matrix[i][j] == 1:
        return False

    # recursive case
    at_origin = (i == 0 and j == 0)
    if at_origin or helper(matrix,i-1,j,path) or helper(matrix,i,j-1,path):
        path.append((i,j))
        cache[(i,j)] = True
        return True
    cache[(i,j)] = False
    return False
        
# Solution: In the matrix, let 0 represent a square can be moved to
# and let 1 represent a square that cannot be moved to. In DP terms,
# the subproblem at each step in the recursion is if you are at
# matrix[i][j] and are either at the origin, can move to matrix[i-1][j],
# or can move to matrix[i][j-1], then store where you currently are
# in the (only) path array and return True. Assuming r is the number
# of rows and c is the number of columns, without memoization the
# time complexity is O(2^(r+c)), since you are making 2 recursive calls
# in each step of the recursion and are doing so at r+c places (that's
# how long a path is), and space complexity is O(1). With memoization,
# time complexity is O(rc) and space complexity is O(rc).
# 
# Note: this problem can also be done with BFS (which would yield same
# time and space complexity is the memoized version above) and would 
# probably be easier that way, but was done with DP for practice.
