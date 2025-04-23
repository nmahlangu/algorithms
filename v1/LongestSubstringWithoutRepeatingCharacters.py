# Given a string, find the length of the longest substring without repeating characters. 
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", 
# which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        i = max_so_far = 0
        seen = {}
        for j in xrange(len(s)):
            if s[j] in seen:
                max_so_far = max(max_so_far,j-i)
                while s[i] != s[j]:
                    del seen[s[i]]
                    i += 1
                i += 1
            else:
                seen[s[j]] = 1
        max_so_far = max(max_so_far,len(s)-i)
        return max_so_far

# Solution:
# Make a simple table to store the characters that have appeared. 
# As you traverse through the string, update by using its ASCII value as index to the table.
# When you have found a repeated character (let’s say at index j), it means that the current substring 
# (excluding the repeated character of course) is a potential maximum, so update the maximum if necessary. 
# It also means that the repeated character must have appeared before at an index i, where i is less than j.
# Since you know that all substrings that start before or at index i would be less than your current maximum, 
# you can safely start to look for the next substring with head which starts exactly at index i+1.
# Therefore, you would need two indices to record the head and the tail of the current substring. Since i and j 
# both traverse at most n steps, the worst case would be 2n steps, which the run time complexity must be O(n).

    