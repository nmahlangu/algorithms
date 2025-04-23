# Given a binary search tree of integers and a target, return the
# number that is closest to the target in the binary search tree.

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def find_closest(node,target):
    if not node:
        return -1
    return find_helper(node,target,float('inf'))
    
def find_helper(node,target,closest):
    # base case
    if not node:
        return closest
    elif node.value == target:
        return target

    # recursive case
    if abs(node.value-target) < abs(closest-target):
        closest = node.value
    
    if target < node.value:
        return find_helper(node.left,target,closest)
    else:
        return find_helper(node.right,target,closest)

# Solution: Traverse the tree as you normally would when searching
# for a target in a binary search tree, but keep track of the closest 
# element you've seen so far as a parameter to your recursion. Return
# the closest element you've seen so far in the base case (when you
# reach the bottom of the tree, aka a None/Null node). Time complexity
# is O(log(n)) and space complexity is O(1).
