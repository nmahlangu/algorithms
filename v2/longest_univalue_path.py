class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        max_length: list[int] = [0]
        self.lup_helper(node=root, max_length=max_length)
        return max_length[0]
    
    def lup_helper(self, node: TreeNode, max_length: list[int]) -> int:
        if node is None:
            return 0

        left_len: int = self.lup_helper(node=node.left, max_length=max_length)
        right_len: int = self.lup_helper(node=node.right, max_length=max_length)

        left: int = 0
        right: int = 0

        if node.left and node.left.val == node.val: 
            left = left_len + 1
        if node.right and node.right.val == node.val:
            right = right_len + 1

        max_length[0] = max(max_length[0], left + right)
        return max(left, right)



