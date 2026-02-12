from collections import deque


class TreeNode:
    def __init__(self, val: int, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zig_zag(self, root: TreeNode):
        if not root:
            return []

        result: list[list[int]] = []
        queue: deque[TreeNode] = deque([root])
        left_to_right: bool = True

        while queue:
            lvl_len: int = len(queue)
            lvl_vals: deque[int] = deque([])

            for _ in range(lvl_len):
                curr = queue.popleft()

                if left_to_right:
                    lvl_vals.append(curr.val)
                else:
                    lvl_vals.appendleft(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            result.append(list(lvl_vals))
            left_to_right = not left_to_right

        return result
