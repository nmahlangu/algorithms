# The minimum edit distance between two strings is defined as the smallest
# number of operations you have to perform on one string to turn it into
# the other. Write a function that takes 2 strings and returns the minimum
# edit distance between them. The only operations available are 1) adding
# a character, 2) removing a character, and 3) replacing a character.

min_dict = {}

def min_edit_distance(s1,s2):
    # base case
    if not s1:
        return len(s2)
    elif not s2:
        return len(s1)

    # recursive case
    if (s1,s2) in min_dict:
        return min_dict[(s1,s2)]                    # check if previously solved
    elif s1[0] == s2[0]:
        return min_edit_distance(s1[1:],s2[1:])     # chars match
    else:
        a = min_edit_distance(s1,s2[1:])            # add to s1
        b = min_edit_distance(s1[1:],s2),           # remove from s1
        c = min_edit_distance(s1[1:],s2[1:])        # replace in s1
        local_min = 1 + min([a,b,c])
        min_dict[(s1,s2)] = local_min               # memoize result
        return local_min

# Solution: At each step of the recursion, compare the first two characters
# of the strings. If they are the same, then recurse with the rest of both
# strings. If they are not, the fewest edits is given by 1 (for the edit to
# fix the two mismatched first characters) plus the minimum number of edits
# in the rest of the recursion. This minimum number is given by the minimum
# of adding one character to s1 and recursing on s1 and all but the first 
# character of s2, removing one character from s1 and recursing on all but
# the first character of s1 and the rest of s2, or replacing a character in
# s1 and recursing on the all but the first characters of s1 and s2. The
# base case occurs when on one string has been consumed, in which case you
# can just return the length of the remaining other string (since you either
# need to add or delete that many characters). Since there are a lot of
# overlapping subproblems, you can use memoization to improve the time
# complexity. Time complexity is O(m*n) and space complexity is O(m*n).
