# A child is running up a staircase with n steps and can hop either 1 step,
# 2 steps, or 3 steps at a time. Write a function to how many possible ways
# the child can run up the stairs.

cache = {}

def run(n):
    # check for memoized result
    if n in cache:
        return cache[n]

    # base case
    if n == 0:
        return 1
    elif n < 0:
        return 0    

    # recursive case
    num_ways = 0
    for i in xrange(1,4):
        num_ways += run(n-i)
    cache[n] = num_ways
    return num_ways

# Solve top-down with dynamic programming. At each step in the recursion,
# the subproblems are how many possible ways can the child take n-1 steps
# (they take one step at the current recursion level), n-2 steps (they take
# 2 steps at the current recursion level), and n-3 steps (they take 3 steps
# at the current recursion level). Time complexity is O(3n), since there are 
# O(3n) subproblems and with memoization you compute each one only once, and 
# space complexity is O(n), since you are memoizing the number of ways to take 
# steps for up to n steps.
