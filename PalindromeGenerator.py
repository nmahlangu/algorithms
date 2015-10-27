# Given a dictionary, find all pairs of words that, when concatenated 
# together, form a palindrome.
#
# E.g. [(nurses, runs),(none,xenon)]

from sets import Set

def is_palindrome(word):
    if not word:
        return True
    for i in xrange(len(word) / 2):
        if word[i] != word[len(word)-i-1]:
            return False
    return True

def palindrome_gen(words):
    if not words:
        return []
    
    words_set = set(words)
    result = set([])

    for i, item in enumerate(words):
        for j in xrange(len(item)):
            left = item[:j+1]
            right = item[j+1:]
            if left[::-1] in words and is_palindrome(right):
                result.add((min(item,left[::-1]),max(item,left[::-1])))
            elif is_palindrome(left) and right[::-1] in words:
                result.add((min(right[::-1],item),max(right[::-1],item)))
    return result

# Solution: All completed palindromes have the form sub + pal + rev(sub),
# where pal == rev(pal). Thus, iterate through ever word and generate
# ever possible prefix and suffix, where prefix + suffix is the whole
# word. If rev(prefix) is in the set of words and is_palindrome(suffix), 
# then store both words. Else if is_palindrome(prefix) and rev(suffix)
# is in the set of words, then store both words. Time complexity is
# O(n(k^2)), where k is the length of the longest word, and space complexity
# is O(n).
    
    

