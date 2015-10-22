# Variation of 3Sum.py. Given an array and a target, write a function that counts
# the number of unique triples that sum to less than the target.
#
# For example
# [1,2,3,4], 9 -> [(1,2,3),(1,2,4),(1,3,4)] -> 3

def count(arr,target):
    # error checking
    if not arr:
        return 0

    num_tuples = 0
    arr.sort()

    # Count number of triples
    for i in xrange(len(arr)):
        if i == 0 or arr[i] != arr[i-1]:
            start = i + 1
            end = len(arr) - 1 
            while start < end:
                elt_sum = arr[i] + arr[start] + arr[end]
                if elt_sum < target:
                    num_tuples += end - start
                    start += 1
                else:
                    end -= 1
    return num_tuples

# Solution: this is very similar to how you do 3sum (see 3sum.py). Whenever
# you reach a configuration where arr[i] + arr[start] + arr[end] is less
# than the target, you can just add (end - sum) to the overall count since
# that will account for all tuples of the form (arr[i],arr[start],arr[x]), where
# x > start and x <= end. Then increment start and keep going. If arr[i] + 
# arr[start] + arr[end] is ever equal to or greater to the target sum, decrement
# end. Time complexity is O(n^2), where n is the number of elements in the array,
# and space complexity is O(1).
