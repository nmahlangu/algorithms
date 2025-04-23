# You've given 2 strings, an input and a pattern. The input will have only
# alphabetic characters. The pattern can have alphabetic characters, '.'
# which is a wild card that can match any character, and '*' which
# can match any number of the previous character. Write a function where
# given an input and a patter, returns if the input matches the pattern.
#
# Example:
# (xyxy,xyzy)  -> False
# (xy,x.)      -> True
# (xyyyx,xy*x) -> True

def check_input(input,pattern):
    return check_helper(input+"-",pattern+"-")

def match(ch1,ch2):
    return ch1 == ch2 or (ch1 != '-' and ch2 == '.')

def check_helper(input,pattern):
    # base case
    if input[0] == '-':
        if pattern[0] == '-':
            return True
        return False
    
    # recursive case
    if pattern[1] == '*': 
        return check_helper(input,pattern[2:]) or (match(input[0],pattern[0]) and check_helper(input[1:],pattern))
    else:
        return match(input[0],pattern[0]) and check_helper(input[1:],pattern[1:])

# Solution: The above solution is vastly simplified by adding a '-' to the end,
# simulating the NULL terminator which is not available in Python. At each 
# point in the recursion, check the 2nd character of the pattern. If it is
# not a '*', then compare the first characters of both strings and recurse. 
# If it is a '*', then 1) recurse on the input and the rest of the pattern 
# starting on the 3rd character, and 2) compare the first characters of both
# strings and recurse on the rest of the input starting at the 2nd character
# and the pattern. The base case is if the pattern is equal to '-', meaning
# you've reached the end of the string, return if the input is also a '-'.
# Time complexity is O(2^n) where n is the length of input, since at each step 
# of the recursion you're making up to 2 recursive calls and there are
# n characters for which this happens for, and space complexity is O(1).
# Can optimize this by memoizing the results that are calculated. In that
# case, time complexity is O(n*m), where n is the length of input and m
# is the length of pattern, and space complexity is O(n*m).
