# Given an n x n matrix, return True if any zero is reachable from
# any other zero. (Reachable in this case means that you can go from
# zero A to B only by traversing left, up, right, and down. Diagonals
# are not allowed). Note: the matrix is guaranteed to have at least
# one zero.
#
# For example,
# [[0,0,1],
#  [1,0,0],  -> True
#  [0,0,1]]
#
# [[0,0,1],
#  [1,0,0],  -> False
#  [0,1,1]]

from sets import Set

# helper function that takes a coordinate (i,j) and a list
# of adjacent coordinates which contain a zero
def get_neighbors((i,j),arr):
    result = []
    height = len(arr)
    width = len(arr[0])

    if j > 0:
        result.append((i,j-1)) # move left
    if i > 0:
        result.append((i-1,j)) # move up
    if j < width - 1:
        result.append((i,j+1)) # move right
    if i < height - 1:
        result.append((i+1,j)) # move down
    
    return filter(lambda (x,y): arr[x][y] == 0, result)    

def check_matrix(arr):
    if not arr:
        return 

    # count number of zeroes
    target = 0
    start = None
    for i in xrange(len(arr)):
        for j in xrange(len(arr[0])):
            if arr[i][j] == 0:
                if not start:
                    start = (i,j)
                target += 1

    # use BFS to count zeroes
    queue = [start]
    visited = set([])
    num_seen = 0
    while queue:
        elt = queue.pop(0)
        num_seen += 1
        for neighbor in get_neighbors(elt,arr):
            if neighbor not in visited:
                queue.append(neighbor)
        visited.add(elt)
    return num_seen == target

# Solution: Count the number of zeroes in the array. Then, pick
# any zero in the matrix to start at and BFS from that zero, only
# adding other coordinates (i,j) if they contain a zero in them.
# Store coordinates that have already been visited. Time complexity
# is O(n^2), since worst case you visit every element of the array
# and space complexity is O(n^2), since worst case you visit and
# store the index of every element in the array.
