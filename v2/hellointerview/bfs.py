from collections import deque

def bfs(root):
    if not root:
        return []

    queue: deque = deque([root])
    while queue:
        node = queue.popleft()
        if node.left:
            deque.append(node.left)
        if node.right:
            deque.append(node.right)

    return queue