# Given 2 strings, write a function to decide if one is a permutation
# of the other.
# Follow-up: What if you can't use any extra space?
# Cracking The Code: 1.2

def check_perm(s1,s2):
    # error checking
    if not s1 or not s2:
        return False

    s1 = "".join(list(sorted(s1)))
    s2 = "".join(list(sorted(s2)))
    return s1 == s2

# Solution: Sort both strings. If the result is the same, return True,
# else False. Time complexity is O(nlog(n)) and space complexity is
# O(1).

def check_perm(s1,s2):
    # error checking
    if not s1 or not s2:
        return False

    # get ch frequency count in s2
    frequencies = {chr(ord('a')+i):0 for i in xrange(26)}
    for ch in s2:
        frequencies[ch] += 1

    # check frequencies against s1
    for ch in s1:
        frequencies[ch] -= 1
    return filter(lambda x: x != 0,frequencies.values()) == []

# Follow-up solution: Count frequencies for letters in both arrays.
# If they don't match, return False. Else return True. Time complexity
# is O(n) and space complexity is O(n).
