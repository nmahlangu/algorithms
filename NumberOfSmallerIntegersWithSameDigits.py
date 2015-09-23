# Given an integer n, find all the integers less than or equal to n that
# have the same digits

from sets import Set
result = set()

def get_smaller_nums(n):
    if not n:
        return 0
    numbers = []
    tmp = n
    while tmp > 0:
        numbers.append(tmp % 10)
        tmp /= 10
    return get_smaller_nums_helper(n, numbers, 0)

def get_smaller_nums_helper(n, numbers, res):
    if not numbers:
        if res < n:
            global result
            result.add(res)
        return

    for i in xrange(len(numbers)):
        new_nums = [numbers[j] for j in xrange(len(numbers)) if j != i]
        get_smaller_nums_helper(n, new_nums, (res * 10) + numbers[i])

# Solution: Recursively build up every possibe permutation of the numbers.
# When in the base case, check if the result is less than or equal to the
# input. If it is, add it to the resulting set. Time complexity is O(m),
# where m is the number of digits in the input number, space complexity is
# O(1).
