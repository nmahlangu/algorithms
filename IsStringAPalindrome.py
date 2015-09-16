# Write a function that returns True if a string is a palindrome, else False

def is_palindrome(s):
    if not s:
        return False
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

# Solution: Have 2 pointers start at the beginning and end of the string. Repeatedly compare the
# letters at the 2 pointers. If they match, move them towards each other, else return False. Once
# they reach each other or cross, return True. Time complexity is O(n) and space complexity is
# O(1)
