# Given only a string containing character '(' and ')', return a balanced string by deleting
# the fewest number of characters possible. A balanced string is one that has a corresponding
# '(' somewhere after every ')'

def balance(s):
    if s == "":
        return s
    invalid = []
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif s[i] == ')':
            if len(stack) == 0:
                invalid.append(i)  
            else:
                stack.pop()
    new_s = "".join([s[i] for i in range(len(s)) if i not in stack and i not in invalid])
    return new_s

# Solution: Each time you see a '(' push it onto the stack. Each time you see a ')', try to pop
# from the stack. If the stack is empty when trying to pop, the current ')' in the string does not 
# have a corresponding '(', meaning that it can be deleted. Finally, any leftover '(' in the stack
# can also be deleted since they have no corresponding ')' character. 
