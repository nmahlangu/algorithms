# You are given a string of digits and a map (aka dictionary) of letters to 
# numbers, where a = 1, b = 2, c = 3.... z = 26. Write a function that will
# compute the number of valid interpretations of the string.
#
# For example
# '11'  -> ['aa','k']         = 2
# '111' -> ['aaa','ak','ka']  = 3

def count_perms(digits):
    # base case
    if not digits:
        return 1

    # recursive case(s)
    if digits[0] == '0':    # invalid
        return 0
    elif len(digits) == 1:  # 1 char
        return 1
    else:
        count = count_perms(digits[1:])         # case 1
        if int(digits[:2]) <= 26:               # case 2
            count += count_perms(digits[2:])
        return count

# Good solution: Given input string S is of the form abX, where a and b
# are single digits and X is the rest of the string, there are 2 recursive
# subcases. Case 1: a is a digit from 1-9, meaning it can represent some
# character from [a-i]. Case 2: If ab taken together has a value from 10-26,
# it can represent some character [j-z]. This events are mutually exclusive
# so the number of possibe interpretations of abX = (number of possible
# interpretations of bX (Case 1) + number of possible interpretations of X
# (Case 2). Zeroes are a corner case - they don't map to anything so
# a zero should be returned in that case. Time complexity is O(2^n),
# since for a string of length n there are 2 subproblems of size n-1
# and n-2 which are computed, and space complexity is O(n) (due to the
# recursive depth of the stack).

cache = {}
def count_perms(digits,i):
    # base case(s)
    if i in cache:
        return cache[i]
    elif i == len(digits):
        return 1
    
    # recursive case(s)
    if digits[i] == '0':
        count = 0
    elif i == len(digits) - 1:
        count = 1
    else:
        count = count_perms(digits,i+1)
        if int(digits[:2]) <= 26:
            count += count_perms(digits,i+2)
        
    # memoize result
    cache[i] = count
    return count

# Better solution: Same as above, but memoize the results as you
# calculate them. This means that time complexity is now O(n), since
# you only need to compute each subproblem once now, and space
# complexity is O(n), since you have to store each subproblem and
# there are n of them.
