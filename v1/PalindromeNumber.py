# Determine whether an integer is a palindrome. Do this without extra space.
# Could negative integers be palindromes? (ie, -1)
# If you are thinking of converting the integer to string, note the restriction of using extra space.
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", 
# you know that the reversed integer might overflow. How would you handle such case?
# There is a more generic way of solving this problem.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        div = 1
        while (x / div >= 10):
            div *= 10
        while x != 0:
            l = x / div
            r = x % 10
            if l != r:
                return False
            x = (x % div) / 10
            div /= 100
        return True

# Solution: Repeatedly get the first and last digit and compare them to each other. It's easy to
# get the last digit, can just mod by 10. To get the first digit, you just need to divide the number 
# by a power of 10 that is as long as the number (the decimal will get thrown away). If these 2 digits
# are ever not equal, then return False. To throw away the last digit, divide the number by 10. To
# throw away the first digit, mod the number by the power of ten that is as long as the number. 
