# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string 
# is valid. The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" 
# are not.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        stack = []
        matches = {'(':')','{':'}','[':']'}
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack or matches[stack.pop()] != c:
                    return False
        return False if stack else True

# Solution: Keep a stack and push any opening character onto it. If you encounter a closing character
# and what is popped from the stack is not the corresponding open character, the string is invalid.
# If the stack is ever empty before the end of the string or the stack is not empty after the
# last character of the string is read, the string is invalid. 
