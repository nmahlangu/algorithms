# Given a binary tree of integers, write code to store the tree into a list

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def tree_to_array(root):
    if not root:
        return []
    queue = [root]
    result = []
    while queue:    
        elt = queue.pop()
        if elt:
            result.append(elt.value)
            queue.append(elt.right)
            queue.append(elt.left)
        else:
            result.append(None)
    return result

# Solution: Do a preorder (node, left child, right child) traversal, 
# writing each node's value to an array as you see it. When you encounter
# a pointer that leads to no element (e.g. when you access a node's left
# child), write a marker (here None) to the array and go back up
# on level in the recursion. Time complexity is O(n) and space complexity
# is O(n).
