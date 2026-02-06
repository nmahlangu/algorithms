class TreeNode:
    def __init__(self, val: int, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def calculateTilt(self, root: TreeNode):
        tilt: int = 0

        def calc(node: TreeNode) -> int:
            nonlocal tilt
            if not node:
                return 0

            left: int = calc(node.left)
            right: int = calc(node.right)
            tilt += abs(left - right)
            return left + right + node.val

        calc(node=root)
        return tilt
