# Write a recursive function to multiply two numbers without using the * operator.
# You can use addition, subtracting, and bit shifting, but you should minimize
# the number of these operations.

def mult(a,b):
    # handle sign
    negative = False
    if (a > 0 and b < 0) or (a < 0 and b > 0):
        negative = True
    
    # compute result
    smaller = min(a,b)
    bigger = max(a,b)
    result = mult_helper(abs(smaller),abs(bigger))
    return (-1 * result) if negative else result

def mult_helper(smaller,bigger):
    # base case
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger

    # recursive case
    half = mult_helper(smaller >> 1, bigger)
    if smaller % 2 == 0:
        return half + half
    else:
        return half + half + bigger

# Solution: Thinking of this in terms on DP, if we want to calculate
# 8 * 9, we can instead calculate 4 * 9 and double it, or in this case
# return (4 * 9) + (4 * 9). Then to calculate 4 * 9, we can return
# (2 * 9) + (2 * 9). In the case where you're multiplying 2 odd numbers,
# for example 5 * 9, you can calculate (2 * 9) + (2 * 9) + 9. To summarize,
# if the smaller number is even, you want to return half + half, where half
# have the result. If the smaller number is odd, you want to return half +
# half + bigger, where bigger is the larger number. Finally, don't forget
# to handle sign. Time complexity is O(log(n)) and space complexity is O(1). 
# Notice no need to memoize, since not doing any repeated computation.
