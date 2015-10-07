# Given an array of integers, write a function that places all non-zero
# elements in front of all zeroes in the array. This should be done
# in-place.

def remove_zeros(arr):
    if not arr:
        return 0

    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] != 0:
            left += 1
        elif arr[right] == 0:
            right -= 1
        else:
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
            right -= 1
    return arr

# Solution: Have a start pointer at the beginning of the array and have
# an end pointer at the end of the array. Repeat the following while
# the start pointer is at a lower index than the end pointer. If the
# start pointer is pointing to a non-zero element, increment the start
# pointer. Else if the end pointer is pointing to a 0, decrement the
# end pointer. Else, swap the values at the start and end pointer, and
# then increment the start pointer and decrement the end pointer.
# Time complexity is O(n) and space complexity is O(1).                    
