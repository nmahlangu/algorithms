# Given a sorted sequence of integers and a target sum, write a function
# that returns whether a contiguous subsequence of the sequence sums
# up to the total.
#
# sequence  | total
# ----------------
# [1,2,3,4] | 5     -> True
# [1,2,3,4] | 6     -> True
# [1,2,3,4] | 10     -> True
# [1,2,5,9] | 10     -> False


from sets import Set

def contains_total(arr,target):
    if not arr:
        return False

    total = 0
    seen_set = set([])
    for elt in arr:
        total += elt
        seen_set.add(elt)
        if total - target in seen_set:
            return True
    return False

# Solution: Iterate through the list, keeping a running sum and storing
# each element as you see it. If at any point the running sum minus
# the target sum is in array you are building up, return True. Return
# False at the end. Time complexity is O(n) and space complexity is
# O(n).
