# Write an algorithm such that if an element in an m x n matrix
# is 0, its entire row and column are set to zero.

# helper function to zero out a row
def zero_row(arr,row):
    for i in xrange(len(arr[0])):
        arr[row][i] = 0

# helper function to zero out a column
def zero_col(arr,col):
    for i in xrange(len(arr)):
        arr[i][col] = 0

def zero_matrix(arr):
    if not arr:
        return arr

    first_row_has_zero = False
    first_col_has_zero = False

    # check if first row has zero
    for j in xrange(len(arr[0])):
        if arr[0][j] == 0:
            first_row_has_zero = True
            break

    # check if first col has zero
    for i in xrange(len(arr)):
        if arr[i][0] == 0:
            first_col_has_zero = True
            break
    
    # set zeroes in first row and column
    for i in xrange(1,len(arr)):
        for j in xrange(1,len(arr[0])):
            if arr[i][j] == 0:
                arr[i][0] = 0
                arr[0][j] = 0

    # zero out cols using first row
    for j in xrange(1,len(arr[0])):
        if arr[0][j] == 0:
            zero_col(arr,j)

    # zero out row using first col
    for i in xrange(1,len(arr)):
        if arr[i][0] == 0:
            zero_row(arr,i)

    # possibly zero out first row
    if first_row_has_zero:
        zero_row(arr,0)

    # possibly zero out first col
    if first_col_has_zero:
        zero_col(arr,0)

    return arr

arr1 = [[0,1,1],[1,1,1],[0,1,1]]
print zero_matrix(arr1)

# Solution: 
# 1) Check if the first row and first column have any zeroes, and
#    set variables first_row_has_zero and first_row_has_col accordingly
# 2) Iterate through the rest of the matrix, setting arr[i][0] and
#    arr[0][j] to 0 whenever there's a 0 in matrix[i][j]
# 3) Iterate through rest of matrix, zero out row i if there's a zero
#    in matrix[i][0]
# 4) Interate through rest of matrix, zero out column j if there's a
#    zero in matrix[0][j]
# 5) Nullify the first row and column if necessary (based on information
#    from step 1.
# Time complexity is O(n^2) and space complexity is O(1).
