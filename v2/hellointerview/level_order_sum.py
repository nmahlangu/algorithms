from collections import deque


class TreeNode:
    def __init__(self, val: int, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def level_order_sum(self, root: TreeNode) -> list[int]:
        if not root:
            return []

        result: list[int] = []
        queue: deque[TreeNode] = deque([root])

        while queue:
            lvl_len: int = len(queue)
            lvl_sum: int = 0

            for _ in range(lvl_len):
                curr = queue.popleft()
                lvl_sum += curr.val

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            result.append(lvl_sum)

        return result
