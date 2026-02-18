from collections import deque


class TreeNode:
    def __init__(self, val: int, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightmostNode(self, root: TreeNode):
        if not root:
            return []

        result: list[int] = []
        queue: deque[TreeNode] = deque([root])

        while queue:
            lvl_len: int = len(queue)

            curr: None | TreeNode = None
            for _ in range(lvl_len):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            result.append(curr.val)

        return result
