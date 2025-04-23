# Given a binary tree, find the length of the longest path between two leaf nodes

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameter(self, node):
        if not node:
            return 0, 0
        
        l_diameter, l_height = self.diameter(node.left)
        r_diameter, r_height = self.diameter(node.right)
        return max(l_diameter, r_diameter, l_height + r_height), max(l_height, r_height) + 1

# Thinking recursively, the diameter of any node in the tree is the maximum value of 
# a) the diameter of the left subtree b) the diameter of the right subtree c) 1 + height 
# of left subtree + height of right subtree. This above approach is implemented better
# than the naive way since it calculates the height of the tree in the same recursion.
# Time complexity is O(n) and space complexity is O(1).  
