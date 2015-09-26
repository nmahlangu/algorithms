import time

# Given a linked list where every node represents a linked list and contains
# two pointers of its type:
# (i) Pointer to the next node in the main list called the right pointer
# (ii) Pointer to a linked list where this node is head called the down pointer
# All linked lists are sorted
#
# For example, given:
# 5 -> 10 -> 19 -> 28
# |    |     |     |
# V    V     V     V
# 7    20    22    40
# |          |     |
# V          V     V
# 8          50    40
# |                |
# V                V
# 30               45
#
# return a list containing 5 7 8 10 19 20 20 22 30 30 35 40 45

from Queue import PriorityQueue

class Node():
    def __init__(self, value, down=None, right=None):
        self.value = value
        self.down = down
        self.right = right

def flatten(node):
    pqueue = PriorityQueue()
    curr = node
    while curr:
        pqueue.put((curr.value,curr))
        curr = curr.right
    
    head = tail = Node("dummy")
    while not pqueue.empty():
        next = pqueue.get()[1]
        tail.down = next
        tail = next
        next.right = None
        if next.down:
            pqueue.put((next.down.value,next.down))
    return head.down

# Good solution: Throw the head of each linked list into a Priority Queue. Make a dummy
# node to function as the head of the new linked list. Repeatedly dequeue an element,
# add it to the tail of the list (keep a pointer to the end as it grows), making sure
# to add the successor node of the aforementioned element if it has one. Time complexity
# is O(nlog(k)), where k is the number of linked list heads and n is the number of elements
# in all linked lists combined, and space complexity is O(1).

def merge(a, b):
    if not a:
        return b
    elif not b:
        return a

    if a.value < b.value:
        result = a
        result.down = merge(a.down, b)
    else:
        result = b    
        result.down = merge(a, b.down)
    
    return result

def flatten(node):
    if not node or not node.right:
        return node
    return merge(node, flatten(node.right))

# Better solution: You want to merge each individual linked list the recursively
# flattened and merged result of everything to its right. The base case
# for flatten is when there's nothing to the given linked list's right.
# Time complexity is O(n) and space complexity is O(1).
