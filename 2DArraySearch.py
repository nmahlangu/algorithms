# Given a target value and a 2D n x n matrix where each row and column 
# is sorted, write a function that search this matrix for the target value
# and returns True if it's present, else False.

def search(arr,target):
    if not arr:
        return False

    n = len(arr)
    i = 0
    j = n - 1
    while i < n and j >= 0:
        elt = arr[i][j]
        print elt
        if elt == target:
            return True
        elif arr[i][j] < target:
            i += 1
        else:
            j -=  1
    return False

# Solution: Start at the top right element of the matrix. If the target is less
# than that number, you can remove the entire right column since you know the
# element cannot be inside it. Else if the target is greater than that number,
# you can remove the entire top row since you know the element cannot be inside
# it. Else if the target matches that element return True. Repeat this process
# until the element is found or there are no next elements to keep search. 
# Time complexity is O(n) and space complexity is O(1).
