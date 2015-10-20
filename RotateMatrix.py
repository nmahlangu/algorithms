# Given an image represented by an n x n matrix, where each pixel is 4
# bytes, write a method to rotate the image by 90 degrees left and
# a method to rotate the image by 90 degrees to the right.

def transpose(arr):
    if not arr:
        return arr
    
    width = len(arr[0])
    height = len(arr)

    for j in xrange(len(arr[0])-1,0,-1):
        i = 0
        while i < height and j < width:
            tmp = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = tmp
            i += 1
            j += 1
    return arr

def rotate_left(arr):
    if not arr:
        return arr

    # transpose matrix
    arr = transpose(arr)

    # reverse order of the rows
    for i in xrange(len(arr)):
        for j in xrange(len(arr[0])):
            tmp = arr[i][j]
            arr[i][j] = arr[len(arr)-i-1][j]
            arr[len(arr)-i-1][j] = tmp
    return arr

def rotate_right(arr):
    if not arr:
        return arr
    
    # transpose matrix
    arr = transpose(arr)

    # reverse order of the columns
    for i in xrange(len(arr)):
        for j in xrange(len(arr[0])/2):
            tmp = arr[i][j]
            arr[i][j] = arr[i][len(arr[0])-j-1]
            arr[i][len(arr[0])-j-1] = tmp
    return arr

# Solution: To rotate the image left 90 degrees, first transpose
# the image and then reverse the order of the rows. To rotate the
# image right 90 degrees, first transpose the image and then reverse
# the order of the columns. Time complexity is O(n^2), since touch
# each element once during transposition and once during row/column
# swap, and space complexity is O(1) since you can do everything
# in place.
