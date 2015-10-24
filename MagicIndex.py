# A magix index in an array A[0...n-1] is defined to be an index such that A[i] = i.
# Given a sorted array of distinct integers, write a method to find a magic index,
# if one exists, in array A.

def bsearch(arr,left,right):
    # base case
    if right < left:
        return -1

    # recursive case
    mid = (left + right) / 2
    if mid == arr[mid]:
        return mid
    elif mid < arr[mid]:
        return bsearch(arr,left,mid-1)
    else:
        return bsearch(arr,mid+1,right) 

# Solution: Write a modified binary search. If i < arr[i], recurse on the
# left subarray. If i > arr[i], recurse on the right subarray. Otherwise,
# return True. Time complexity is O(log(n)) and space complexity is O(1).
