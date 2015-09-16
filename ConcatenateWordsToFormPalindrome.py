# Given a list of words, return all pairs of words that form a palindrome when concatenated
# For example:
#    words = ["run","nurses","race","car","ma","am", "apple", "a"] should return
#    [('car', 'race'), ('a', 'am'), ('am', 'ma'), ('nurses', 'run')]

from pytrie import SortedStringTrie as trie
from sets import Set

def is_palindrome(s):
    """
    Returns True if string s is a palindrome, else False
    """
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

def get_palindrome_pairs(words):
    t = trie({w[::-1]:0 for w in words})
    result = set()

    for word in words:
        for i in range(1,len(word)+1):
            sub = word[:i]
            if sub == t.longest_prefix(sub,None):
                if i == len(word) or is_palindrome(word[i:]):
                    tup = (min(sub[::-1],word),max(sub[::-1],word))
                    if tup not in result and tup[0] != tup[1]:
                        result.add(tup)
    return result

print get_palindrome_pairs(["run","nurses","race","car","ma","am", "apple", "a"])

# Solution: Create a trie containing all words inserted in reversed order. Then for each original
# word you have, check if any prefix if the word is in the trie. If it is, check if the suffix is
# a palindrome (if there is one). If both of these conditions are true, then add to a set the tuple
# of the reversed prefix (the word in the trie) and the word you're currently checking prefixes
# of (first entry should be ordered first lexigraphically). Assuming k is the length of the longest
# word in our list, time complexity is O(nk) to build the trie and O(n*2k) to check for all pairs, so
# it's O(nk) overall. Space complexity for a trie is given by O(alphabet_size * key_length * n), giving
# us O(26 * k * n) = O(nk).
