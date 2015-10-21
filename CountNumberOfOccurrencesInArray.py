# Given a sorted array and a target, count the number of times the target value
# appears in the array.
#
# For example
# [1,2,2,2,4], 2 -> 3

low = float('inf')
high = -float('inf')

def bsearch(arr,left,right,target):
    # base case
    if right < left:
        return

    # recursive case
    mid = (left+right)/2
    if target == arr[mid]:
        global low, high
        low, high = min(low,mid), max(high,mid)
        bsearch(arr,left,mid-1,target)
        bsearch(arr,mid+1,right,target)        
    elif target < arr[mid]:
        bsearch(arr,left,mid-1,target)
    else:
        bsearch(arr,mid+1,right,target)

def count(arr,target):
    if not arr:
        return 0

    bsearch(arr,0,len(arr)-1,target)
    global low, high

    # element is not in array
    if low == float('inf'):
        return 0
    elif low == high:
        return 1
    else:
        return high-low+1

# Solution: Implement a modified version of binary search as follows. At
# each step of the recursion, calculate the middle index. If the element
# at that index matches the target element, update the lowest and highest
# indices at which you've seen the target element before and recurse into
# both halves of the array (exclusing the middle element). If the target
# element is less than the middle element, recurse into the left subarray.
# Else, recurse into the right subarray. Once you have the lowest and
# highest indices at which you've seen the element, there are 3 cases.
# 1) low = float('inf'), this means you've never seen the element and
# want to return 0. 2) low == high, this means the element showed up once
# and you want to return 1. 3) low and high are different numbers, so you
# want to return their difference plus 1. Time complexity is O(log(n)),
# since you're throwing half of the array away at each step in the
# recursion, and space complexity is O(1).
