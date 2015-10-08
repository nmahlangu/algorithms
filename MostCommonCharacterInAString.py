# Given a string, print the alphabetic letter(s) that appear(s) the most frequently
from sets import Set

def most_common_chars(s):
    if not s:
        return []

    valid_chars = set([chr(ord('a')+i) for i in xrange(26)])
    map = {}
    for ch in s:    
        if ch in valid_chars:
            map.setdefault(ch,0)
            map[ch] += 1

    if map.keys() != []:
        max_count = max(map.values())
        return [ch for ch in map.keys() if map[ch] == max_count]
    return []

print most_common_chars("assff")
# Solution: Hash each letter as you pass through the string, incrementing
# each letter's count every time you see it. Determine the highest occurrence
# by 1 or more letters and return those letters. Time complexity is O(n)
# and space complexty is O(n).
