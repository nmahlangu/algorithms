class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDiameter(self, root: TreeNode):
        max_seen: list[int] = [0]
        self._maxDiameter(root, max_seen)
        return max_seen[0]
    
    def _maxDiameter(self, root: TreeNode, max_seen: list[int]):
        # base case
        if not root:
            return 0

        # recursive case
        left: int = self._maxDiameter(root.left, max_seen)
        right: int = self._maxDiameter(root.right, max_seen)
        max_seen[0] = max(max_seen[0], left + right)
        return 1 + max(left, right)