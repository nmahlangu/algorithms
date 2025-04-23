# Implement atoi to convert a string to an integer.
# Hint: Carefully consider all possible input cases. 
# If you want a challenge, please do not see below and ask yourself what are the possible input cases.
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). 
# You are responsible to gather all the input requirements up front.
#
# Requirements for atoi:
# The function first discards as many whitespace characters as necessary until the first non-whitespace 
# character is found. Then, starting from this character, takes an optional initial plus or minus sign 
# followed by as many numerical digits as possible, and interprets them as a numerical value.
# The string can contain additional characters after those that form the integral number, which are ignored 
# and have no effect on the behavior of this function. If the first sequence of non-whitespace characters in 
# str is not a valid integral number, or if no such sequence exists because either str is empty or it contains 
# only whitespace characters, no conversion is performed.
# If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range 
# of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str or len(str) < 1:
            return 0
        str = str.lstrip()
        positive = True if str[0] != '-' else False
        str = str[1:] if str[0] == '+' or str[0] == '-' else str
        sum = 0
        for i in range(len(str)):
            if ord(str[i]) < ord('0') or ord(str[i]) > ord('9') or ord(str[i]) == ord(' '):
                break
            sum = (sum * 10) + (ord(str[i]) - ord('0'))
            if positive and sum > (2**31)-1:
                return (2**31)-1
            elif not positive and sum > (2**31):
                return -1 * (2**31)
        return sum if positive else (-1 * sum)

# Solution: Error check for leading spaces and a '+' or '-' sign. After that, convert each char
# to an int, if it's invalid, stop parsing and return the running sum. Otherwise, add the new
# number to the result * 10. Time complexity is O(n), space complexity is O(1).
