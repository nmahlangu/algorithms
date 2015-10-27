# Write a function to compute all permutations of a string whose characters
# are not necessarily unique. The list of permutations should not have
# duplicates.

result = []

def perms(s):
    if not s:
        return []
    letters = list(sorted([ch for ch in s]))
    perms_helper(letters,"")

def perms_helper(arr,tmp):
    # base
    if not arr:
        global result
        result.append(tmp)
        return

    # recursive
    for i in xrange(len(arr)):
        if i == 0 or arr[i] != arr[i-1]:
            new_arr = [arr[j] for j in xrange(len(arr)) if i != j]
            perms_helper(new_arr,tmp+arr[i])

# Solution: Similar to the regular problem, but in the recursive step,
# only go down a path in the "recursive tree" if the next letter you're
# taking doesn't match the previous one. Time complexity is O(n!), since
# worst case all the letters are unique, and space complexity is O(1),
# assuming you're not storing the intermediate results (e.g. you're just
# printing them), otherwise it's O(n!) as well.
