# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321
# 
# Have you thought about this?
# Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!
# If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.
# Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 
# 1000000003 overflows. How should you handle such cases?
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

import sys

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
	positive = True
	if x < 0:
		positive = False
		x *= -1
	ans = 0
	while x > 0:
		ans = (ans * 10) + (x % 10)
		if ans > (2**31)-1:
			return 0
		x /= 10
	return ans if positive else (-1 * ans)   

# Solution: Continually mod off the last number and each time add it to the current sum * 10. 
# If the number is ever greater than INT_MAX, the number overflowed (and python cast it to 
# another type) meaning you should return zero. Time complexity is O(n), space complexity is
# O(1). 
