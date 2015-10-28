# Given a string, write a function to calculate the length of the longest
# substring which does not have duplicated characters. You can assume
# that all characters in the string are alphabetic.

def count(s):
    if not s:
        return 0

    last_seen = {}
    curr_len = 0
    max_len = 0
    
    for i in xrange(len(s)):
        # not a duplicate character
        if s[i] not in last_seen:
            curr_len += 1
        # previous matching latter is not in substring
        # ending with s[i]
        elif i - last_seen[s[i]] > curr_len:
            curr_len += 1                    
        # distance to matching letter is length of
        # the substring ending with s[i]
        else:         
            max_len = max(max_len,curr_len)
            curr_len = i - s[i]
        s[i] = i
    return max_len

# Solution: Denote the length of the longest substring ending with
# the ith character (0 indexed) L(i). Letting p(s[i]) denote the index
# of the previous occurrence of character s[i]. Then L(i) can be written as
# follows L(i) = { (1) 1+L(i-1) if s[i] has not been seen before
#                  (2) 1+L(i-1) if i - p(s[i]) > L(i-1)
#                  (3) i - p(s[i]) otherwise
#
# Cases:
# (1) If a letter hasn't been seen before, increment current length by 1
# (2) If the distance between the 2 repeated letters is greater than
#     the length of the current substring ending at s[i], then the first 
#     occurrence of the letter is not in the current substring. Thus,
#     increment current length by 1
# (3) If the distance between the 2 repeated letters is less than
#     the length of the current substring ending at s[i], then current
#     length is the distance between the 2 repeated letters.
# 
# Time complexity with dynamic programming is O(n) and space complexity
# is O(1).
