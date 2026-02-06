import copy

class TreeNode:
    def __init__(self, val: int, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> list[list[int]]:
        result: list[list[int]] = []
        self.pathSumHelper(node=root, target=target, path=[], result=result)
        return result

    def pathSumHelper(
        self,
        node: TreeNode,
        target: int,
        path: list[int],
        result: list[list[TreeNode]],
    ) -> None:
        if not node:
            return 

        target -= node.val
        path.append(node.val)

        if node.left is None and node.right is None:
            if target == 0:
                result.append(path[:])

        self.pathSumHelper(node=node.left, target=target, path=path, result=result)
        self.pathSumHelper(node=node.right, target=target, path=path, result=result)
        path.pop()

