# Given an array of integers, we would like to determine whether the array is monotonic (non-decreasing/non-
# increasing) or not.

def is_monotonic(arr):
    if not arr or len(arr) == 1:
        return True

    increasing = True if arr[0] < arr[-1] else False
    prev = arr[0]
    for i, item in enumerate(arr[1:]):
        if item < prev and increasing:
            return False
        elif item > prev and not increasing:
            return False
        prev = item
    return True

# Solution: Compare the first and the last element to see if the array should be
# mononically increasing or decreasing. Store the first element as the previous
# element. Iterate through the array and for each element, if the element is greater
# than the previous one but the array is decreasing, or if the element is less
# than the previous one but the array is increasing, return False. Else, update
# the previous element to be the currrent element and keep going. Return True
# if you make it to the end with no errors.
