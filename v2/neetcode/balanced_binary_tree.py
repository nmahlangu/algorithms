from typing import Optional
from typing import Tuple    

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        (_,r) = self.calc_depths(root)
        return r

    # int = height of longest sub tree
    # bool = if the subtrees from current node are balanced
    def calc_depths(self, node: Optional[TreeNode]) -> Tuple[int, bool]:
        # base
        if not node:
            return (0,True)

        # recursive
        l_depth, l_valid = self.calc_depths(node.left)
        r_depth, r_valid = self.calc_depths(node.right)

        is_valid = self.is_balanced(l_depth, r_depth) and l_valid and r_valid
        depth = max(l_depth, r_depth) + 1 

        return (depth, is_valid)  

    def is_balanced(self, depth_a: int, depth_b: int):
        return abs(depth_a - depth_b) <= 1