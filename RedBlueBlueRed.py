# You're given two strings, 'pattern' and 'input', e.g.
# pattern: "abba"
# input: "redbluebluered"
# This example is considered a match because the patter of the words in 'input'
# matches the pattern of characters in 'pattern'. The pattern specifies that
# you have an instance of one word, two instances of another word, and another
# instance of the first word. Furthermore, the input doesn't have to contain
# english words. This means that "abcxyzxyzabc" should still return true when
# the pattern is "baab", "abba", "dzzd", etc.

import copy
from sets import Set

def check_pattern(pattern,input):
    letters = set([])
    for ch in pattern:
        if ch not in letters:
            letters.add(ch)
    return check_helper(pattern,input,letters,{},"")

def check_helper(pattern,input,letters,dict,result):
    # base case
    if result != pattern[:len(result)]:
        return False
    elif len(pattern) == len(result):
        if not input and pattern == result:
            return True
        return False

    # recursive case
    for i in xrange(1,len(input)+1):
        sub = input[:i]
        if sub in dict:
            if check_helper(pattern,input[i:],letters,dict,result+dict[sub]):
                return True
        else:
            for ch in letters:
                new_dict = copy.deepcopy(dict)
                new_dict[sub] = ch
                new_letters = [let for let in letters if let != ch]
                if check_helper(pattern,input[i:],new_letters,new_dict,result+ch):
                    return True
    return False

# Solution: In each step of the recursion, iterate through the input. During the iteration,
# consider the substring input[:i]. Case 1: input[:i] has not been seen before, so iterate 
# through the potential remaining letters assigning the substring to it, and recurse on the
# rest of the string, making sure to store which letter was used for the substring in a 
# dictionary passed to that recursion and append the letter to the result being built up. 
# Case 2: input[:i] has been seen before. Fetch it's corresponding letter from the dictionary 
# and recurse on  the rest of the string, making sure to append the letter to the result
# that's being up. The base case has a few parts. First, if the result being built up does 
# not match the pattern, you can return False immediately since it will never be correct.
# Second, once the result is the length of the pattern, if it matches you can return True,
# else False, since there's no use in building up a longer result.
