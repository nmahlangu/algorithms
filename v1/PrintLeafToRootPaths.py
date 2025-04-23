# Given a binary tree, print all paths from the root to a child.
# 
# For example:
#           A
#         /   \
#        B     C
#       / \   / \
#      D   E F   G
# 
# Output would be DBA,EBA,FCA,GCA

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def print_paths(node):
    if not node:
        return
    print_helper(node,"")

def print_helper(node,result):
    if not node:
        return

    result = node.value + result
    if not node.left and not node.right:
        print result
    else:
        print_helper(node.left,result)
        print_helper(node.right,result)

# Solution: Recursively do a DFS down the tree and pass along the
# path so far at each step of the recursion. Once you reach a node
# that has no children, print the value of the current node + the
# path so far, otherwise. Because this problem takes into account
# the time to build and print the path, we have to consider that
# in our runtime. Furthermore, python strings are immutable so it
# creates a new string whenever concaenation is done. In balanced 
# binary trees, time complexity is O(nlog(n)), since the path you 
# print out will be of length log(n), (that's the height of a 
# balanced tree); in a linked-list like tree, time complexity is 
# O(n^2) since the longest path will be of length n. Space complexity 
# is O(1). However, ignoring printing the time complexity is O(n)
# and the space complexity is O(1).
