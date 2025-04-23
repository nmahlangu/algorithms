# Given a set of coins and a target value, write a function that
# returns the fewest number of coins needed to make change for the
# target value. 

cache = {}

def count(coins,target):
    # memoization
    global cache
    if target in cache:
        return cache[target]

    # base case
    if target == 0:
        return 0

    # recursive case
    fewest = float('inf')
    for coin in coins:
        if target - coin >= 0:
            fewest = min(fewest,1+count(coins,target-coin))
    cache[target] = fewest
    return fewest

# Solution: Define f(i) to be the function that given the minimum
# number of coins for target value i. The function f can then be
# written as f(i) = { 0 if i == 0
                      min(1+f(i-coins[j])) where 0 < j < len(coins)
# Using memoization, time complexity is O(coins * target) and space
# complexity is O(target).
