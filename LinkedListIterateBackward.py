# Iterate over a singly linked list backwards. Call print on each node.
# Reverse a singly linked list.

class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# recursive solution
def iterate_backwards(node):
    if not node:
        return

    iterate_backwards(node.next)
    print node.value

# Solution: A basic recursive function where the base case is to return if the node
# is None, and the recursive case is to recurse to the next element and print out
# the current element. Time complexity is O(n) and space complexity is O(1).
# Weaknesses: May cause a stack overflow. Setup for stack on each recursive call
# is the caller's %ebp, caller's return address, and then the parameters for the
# callee.

def iterate_backwards(node):
    stack = []
    current = node
    while current:
        stack.append(current)
        current = current.next
    while stack:
        print(stack.pop(-1).value)

# Solution: Push each element onto a stack and then pop from the stack until empty,
# printing the result of the pop as you do along. Time complexity is O(n) and space
# complexity is O(n). Another option is to use a linked list. While a stack, (aka
# array) has good locality and no space overhead, it requires reallocation. On the
# other hand, a linked list requires no reallocation overhead, but has poor memory
# locality and uses more memory. Useful to know: the word size refers to the size
# of a processor register (e.g. on a 32-bit OS it would be 32 bits).

def iterate_backwards(node):
    last = None
    while node != last:
        current = node
        while curr.next != last:
            curr = curr.next
        print curr.value
        last = curr

# Solution: Have a pointer which always points to the end of the list. Traverse
# to just before it on every iteration and print the element before it. Do this
# until the last element is pointed to by the head of the list. Time complexity
# is O(n^2) and O(1) space.
    
def reverse_list(node):
    head = Node("dummy")
    current = node
    while current:
        tmp = current.next    
        current.next = head.next
        head.next = current
        current = tmp
    return head.next

# Solution: Create a dummy head and repeatedly get the first element from
# the list and attach it to the head's next pointer. Time complexity
# is O(n) and space complexity is O(1).


