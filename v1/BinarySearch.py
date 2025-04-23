# Implement binary search

def bsearch(arr,target,left,right):
    # base case
    if right < left:
        return False

    # recursive case
    mid = (left + right) / 2
    if target == arr[mid]:
        return True
    elif target < arr[mid]:
        return bsearch(arr,target,left,mid-1)
    else:
        return bsearch(arr,target,mid+1,right)

# Time complexity is O(log(n)), since you're throwing half the
# problem away at each step in the recursion, and space complexity
# is O(1).
