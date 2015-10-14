# Given an n x m matrix, print it in spiral form.
#
# For example, for the matrix,
# [[1,2,3,4],
#  [5,6,7,8],
#  [9,10,11,12]]
# 
# Print
# 1 2 3 4 8 12 11 10 9 5 6 7

def print_spiral(arr):
    if not arr:
        return 

    top = 0
    left = 0
    bottom = len(arr)
    right = len(arr[0])
    
    while top < bottom and left < right:
        # first remaining row
        for i in xrange(left,right):
            print arr[top][i],
        top += 1
    
        # last remaining column
        for i in xrange(top,bottom):
            print arr[i][right-1],
        right -= 1

        # last remaining row
        if top < bottom:
            for i in xrange(right-1,left-1,-1):
                print arr[bottom-1][i],
            bottom -= 1
    
        # first remaining column
        if left < right:
            for i in xrange(bottom-1,top-1,-1):
                print arr[i][left],
            left += 1

    print

# Solution: Store a variable for the left and top boundaries of the matrix
# (inclusive) and store a variable for the right and bottom boundaries
# of the matrix (exclusive). Print the first remaining row by iterating from
# the left to right boundary, and increment the top boundary after. Print the 
# last remaining column by iterating from top to bottom, decrementing the right
# boundary after. If the top boundary is less than the bottom boundary, print
# the last remaining row by iterating from right-1 to left-1, and decrement
# the bottom boundary after. If the left boundary is less than the right boundary,
# iterate from bottom-1 to top-1, incrementing the left boundary after. 
# Time complexity is O(n*m) and space complexity is O(1).
