# Given an integer c, return tuple (a,b)  such that a^2 + b^2 = c. If this is
# not possible, return (-1,-1).

import math

def pythagorean(c):
    # error checking
    if c <= 0:
        return (-1,-1)

    start = 1
    end = int(math.sqrt(c))
    while start <= end:
        var_sum = start**2 + end**2
        if var_sum == c:
            return (start,end)
        elif var_sum < c:
            start += 1
        else:
            end -= 1
    return (-1,-1)

# Solution: The bounds of numbers that [a,b] can be in are [1,sqrt(c)],
# so initialize a as 1 and b as sqrt(q). Repeat the following until b < a. 
# Compute the sum of a^2 + b^2. If it's less than c, increment a. If it's 
# greater than target, decrement b. If it's equal to c, return (a,b).
# Time complexity is O(sqrt(c)) and space complexity is O(1).
