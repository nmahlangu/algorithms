# Given an array of elements, write an iterative and recursive function
# to generate the powerset of the array.

def iter_powerset(arr):
    result = []
    for i in xrange(2 ** len(arr)):
        num = i
        partial = []
        j = 0

        while num > 0:
            if num & 1:
                partial.append(arr[j])
            j += 1
            num >>= 1
            
        result.append(partial)
    return result

# Solution: Generate all numbers from 0 to 2^n, where n is the length of
# the array. For each of these numbers, add a subarray to the result containing
# all the elements at the indices that are a 1 in the number. Time complexity
# is O(2^n) and space complexity is O(2^n).

import copy

def rec_powerset(arr):
    # base case
    if not arr:
        return [[]]

    # recursive case    
    rest = rec_powerset(arr[1:])
    curr = map(lambda x: x + [arr[0]],copy.deepcopy(rest))
    return rest + curr

# Solution: At each step in the recursion, you want to return the
# powerset without the current element combined with the current
# element appended to every element in the powerset. The base case
# is when you have no more elements, in which case you return [[]].
# Time complexity is O(2^n) and space complexity is (O2^n)
