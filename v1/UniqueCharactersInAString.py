# Implement an algorithm to determine if a string has all unique characters.
# Follow-up: what if you can't use an external data structure?
# Source: Cracking The Code 1.1

def unique(s):
    # error checking
    if not s:
        return True

    chars = {}
    for ch in s:
        chars.setdefault(ch,0)
        chars[ch] += 1
        if chars[ch] > 1:
            return False
    return True

# Solution: Keep a dictionary where keys are the letters seen so far
# and values are number of times a letter has been seen. Update this
# dictionary when iterating through the string and if a letter has been
# seen more than once when handling it, return False. Time complexity
# is O(n) and space complexity is O(n).

def unique(s):
    if not s:
        return True

    s = "".join(list(sorted(s)))
    for i in xrange(len(s)):
        if i > 0 and s[i] == s[i-1]:
            return False
    return True

# Follow-up Solution: Sort the string. If any adjacent characters match,
# return False. Otherwise, return True. Time complexity is O(nlog(n)) and
# space complexity is O(1).
