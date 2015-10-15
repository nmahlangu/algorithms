# Given a sorted list of coin values and a target sum, return the different
# combinatinos of the coins will yield the target sum.
#
# For example:
# coinDenominations([1,2],5)
# - [1,1,1,1,1]
# - [1,1,1,2]
# - [1,2,2]

answer = []

def coinDenominations(coins,target):
    if not coins or not target:
        return 0
    coin_helper(coins,target,[])
    
def coin_helper(coins,target,result):
    # base case
    if not target:
        answer.append(result)
        return  
    
    # recursive case
    for i in xrange(len(coins)):
        if coins[i] <= target:
            coin_helper(coins[:i+1],target-coins[i],result+[coins[i]])

# Solution: The naive way of doing this is to deduplicate solutions after
# you construct them (e.g. you don't want to count both [2,2,1] and [1,2,2]
# in the example above). Thus, you can impose the invariant that you're only
# allowed to use coins of equal or less value to the smallest coin in the
# current subproblem. Time complexity is O(c^m), where c is the number of
# coins you are given, and space complexity is O(1) (ignoring the array
# storing the solution).
