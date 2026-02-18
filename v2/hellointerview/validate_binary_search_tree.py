class TreeNode:
    def __init__(self, val: int, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def validateBST(self, root: TreeNode):
        return self.validate(node=root, min_val=float("-inf"), max_val=float("inf"))

    def validate(self, node: TreeNode, min_val: float, max_val: float) -> bool:
        if not node:
            return True

        if node.val <= min_val or node.val >= max_val:
            return False

        left: bool = self.validate(node=node.left, min_val=min_val, max_val=node.val)
        right: bool = self.validate(node=node.right, min_val=node.val, max_val=max_val)
        return left and right
