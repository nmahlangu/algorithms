# Write a function to find the longest common prefix string amongst an array of
# strings. 

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        min_len = len(min(strs,key=len))
        if min_len == 0:
            return ""
        else:
            for j in range(min_len):
                prev_ch = ""
                for i in range(len(strs)):
                    if i == 0:
                        prev_ch = strs[i][j]
                    else:
                        if strs[i][j] != prev_ch:
                            return strs[i][:j]
            return strs[0][0:min_len]

# Solution: Find the length of the minimum word in the array. Loop over that many characters
# in each word, checking to see if the ith character is the same at every point. If one ever
# differs, return 0th to the i-1th character in any string.

