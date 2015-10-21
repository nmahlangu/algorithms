# Given an n x m matrix, print the diagonals of the matrix.
#
# For example for the matrix
# [[1,2,3],
#  [4,5,6],
#  [7,8,9]]
#
# you should print:
# 3
# 2 6
# 1 5 9
# 4 8
# 7

def print_diag(arr):
    if not arr:
        return 

    n = len(arr)
    m = len(arr[0])

    # go along first row
    for k in xrange(m-1,-1,-1):
        i = 0
        j = k
        while i < n and j < m:
            print arr[i][j],
            i += 1
            j += 1
        print

    # go along first column
    for k in xrange(1,n):
        i = k
        j = 0
        while i < n and j < m:
            print arr[i][j],
            i += 1
            j += 1
        print

# Solution: Iterate over the first row in reverse and for each iteration,
# repeatedly print array[i][j] and increment i and j while you stay within
# the bounds of the array. Then, iterate over the first column (starting at
# the second row) and for each iteration, repeatedly print array[i][j] and 
# incrememnt i and j while you stay within the bounds of the array. Time
# complexity is O(nm) and space complexity is O(1).
