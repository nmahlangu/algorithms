from collections import deque

class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxWidth(self, root: TreeNode):
        if not root:
            return 0

        max_width: int = 0
        queue: deque[(TreeNode, int)] = deque([(root, 0)])

        while queue:
            lvl_len: int = len(queue)

            lvl_left: (TreeNode, int) = queue[0]
            lvl_right: (TreeNode, int) = queue[-1]

            for _ in range(lvl_len):
                curr_node, curr_pos = queue.popleft()

                if curr_node.left:
                    queue.append((curr_node.left, 2 * curr_pos))
                if curr_node.right:
                    queue.append((curr_node.right, (2 * curr_pos) + 1))

            max_width = max(max_width, lvl_right[1] - lvl_left[1] + 1)

        return max_width

