# Given a string, write a function to check if it is a permutation of
# a palindrome. A palindrome is a word or phrase that is the same
# forwards and backwards. A permutation is a rearrangement of letters.
# Note: the palindrome does not need to be limited to just dictionary
# words. Ignore spaces.

def pal_perm(s):
    if not s:
        return False
    
    frequencies = {}
    for ch in s:
        if ch != " ":
            frequencies.setdefault(ch,0)
            frequencies[ch] += 1
    return len(filter(lambda x: x % 2 != 0,frequencies.values())) < 2

# Count the frequency of every letter. All palindromes are in the form
# prefix + mid + suffix, where reversed(prefix) == suffix and mid is
# either the empty string or a single letter. Thus, return False if
# the frequency of more than one letter is odd, else True. Time
# complexity is O(n) and space complexity is O(n).
