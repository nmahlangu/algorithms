# Given an integer c, return tuple (a,b) such that a^2 + b^2 = c. If this is
# not possible, return (-1,-1).

import math

def pythagorean(c):
    # error checking
    if c < 0:
        return (-1,-1)

    # case 1
    var_sum = int(math.sqrt(c))
    if var_sum == math.sqrt(c):
        return (var_sum,var_sum)

    # case 2
    start = 1
    end = int(math.sqrt(c))
    while start < end:
        var_sum = start**2 + end**2
        if var_sum == c:
            return (start,end)
        elif var_sum < c:
            start += 1
        else:
            end -= 1
    return (-1,-1)

# Solution: First check if sqrt(c) is an integer - if it is, return (c,c).
# Else, we know the bounds of numbers that [a,b] can be in are [0,sqrt(c)],
# so initialize a as 1 and b as sqrt(q). Repeat the following until b < a. 
# Compute the sum of a^2 + b^2. If it's less than c, increment a. If it's 
# greater than target, decrement b. If it's equal to c, return (a,b).
# Time complexity is O(sqrt(c)) and space complexity is O(1).
