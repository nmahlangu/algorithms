# Given a string S, find the longest palindromic substring in S. You may assume 
# that the maximum length of S is 1000, and there exists one unique longest palindromic 
# substring.
# 
# Note: A palindrome is a word which reads the same in both directions

class Solution:
    def expandFromCenter(self,s,l,r):
        n = len(s)
        while (l >= 0 and r <= n-1) and (s[l] == s[r]):
            l -= 1
            r += 1
        return s[l+1:r] # simplified from s[l+1:r-1+1]

    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        n = len(s)
        if n == 0:
            return ""
        longest = s[0]
        for i in range(n-1):
            p1 = self.expandFromCenter(s,i,i)
            p2 = self.expandFromCenter(s,i,i+1)
            p = max(p1,p2,key=len)
            longest = max(p,longest,key=len)
        return longest

# Solution: 
#   We observe that a palindrome mirrors around its center. 
#   Therefore, a palindrome can be expanded from its center, and there are
#   only 2N-1 such centers. The reason there are this many is because the
#   center of a palindrome can be a letter, or between two letters. There
#   are N letters and N-1 spaces between letters, thus giving us 2N-1 places
#   to check. Since checking from a center takes O(n) time, we have a time
#   complexity of O(n^2) and space complexity of O(1). 


# Other Solutions
# 1) Brute Force: nC2 combinations of indices in the string, try each one
#    and see if it's a palindrome while keeping track of the longest one.
#    O(n^2) strings and doing O(n) work for each of them, so 
#    O(n^3) time and O(1) space.
#
# 2) Dynamic Programming: Let s be the input string, i and j are indices of
#    the string. Define a 2-dimension array "table" and let table[i][j]
#    denote whether a substring from i to j is a palindrome.
#    Start Condition:
#       table[i][i]   = 1
#       table[i][i+1] = 1 if s[i] == s[j]
#    Changing condition:
#       table[i][j]   = 1 if table[i+1][j-1] && s[i] == s[j]
#
#    O(n^2) space to calculate each value and O(n^2) space to store the value
