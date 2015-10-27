# Write a function to print all valid (e.g. properly opened and closed)
# combinations of n pairs of parenthesis.
# 
# Example:
#   Input: 3
#   Output: [((())),(()()),(())(),()(()),()()()]

result = []

def parens(n):
    if not n:
        return

    parens_helper(n,n,"")

def parens_helper(open,close,tmp):
    # base case
    if open == close == 0:
        global result
        result.append(tmp)
        return

    # recursive case        
    if open > 0:
        parens_helper(open-1,close,tmp+'(')
    if close > open:
        parens_helper(open,close-1,tmp+')')
    
# Solution: Thinking of this in terms of DP, there are 2 subproblems
# to think about here. The first is if you can add an open parenthesis
# and recurse on that, and this can be done as long as we still have
# open parentheses left. The second subproblem is if you can add a
# closed parenthesis and recurse on that, and this can be done as long
# as the number of close parenthesis is greater than the number of open
# parenthesis.
