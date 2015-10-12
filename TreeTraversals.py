# Write a function for a pre-order DFS traversal, an in-order DFS traversal and a
# post-order DFS traversal of a binary tree. Second, write a function for a BFS
# traversal of a binary tree.

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

a = Node('a')
a.left = Node('b')
a.left.left = Node('d')
a.left.right = Node('e')
a.right = Node('c')
a.right.left = Node('f')
a.right.right = Node('g')

########################## DFS ##########################

# preorder
def preorder(node):
    if not node:
        return

    print node.value,
    preorder(node.left)
    preorder(node.right)

def preorder_iter(node):
    if not node:
        return

    stack = []
    while stack or node:
        if node:
            print node.value,
            stack.append(node.right)
            node = node.left
        else:
            node = stack.pop()

# inorder
def inorder(node):
    if not node:
        return
    
    inorder(node.left)
    print node.value,
    inorder(node.right)

def inorder_iter(node):
    if not node:
        return

    stack = []
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print node.value,
            node = node.right

# postorder
def postorder(node):
    if not node:
        return

    postorder(node.left)
    postorder(node.right)
    print node.value,

def postorder_iter(node):
    if not node:
        return

    stack = []
    last_visited = None
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            peek_node = stack[-1]
            # if right child exists and traversing node from left child,
            # move to the right child
            if peek_node.right and last_visited != peek_node.right:
                node = peek_node.right
            else:
                print peek_node.value,
                last_visited = stack.pop()

# Solution: The X-order part is describing where in the traversal you
# do, in this case, the printing. So in pre- you do it before both nodes,
# in in- you do it between both nodes, and in post- you do it after both
# nodes. Use a stack to keep track of nodes that need to be visited.
# 
# Iterative:
# The time complexity of each of these implementations is O(v), where v 
# is the number of edges, and the space complexity is O(v) (since in the 
# worst case you hold every vertex in your stack).
#
# Recursive:
# The time complexity of each of these implementations is O(v), where v
# is the number of edges, and the space complexity is O(h), where h is
# the maximal depth of the tree (this space will be used in memory
# stack space, not a stack data structure like the iterative implementations).

########################## BFS ##########################

def bfs(node):
    if not node:
        return

    queue = [node]
    while queue:
        elt = queue.pop(0)
        if elt:
            print elt.value,
            queue.append(elt.left)
            queue.append(elt.right)

# Solution: Handle the current node and then use then append it's children
# to the queue being used to keep track of which nodes to visit next. Time
# complexity is O(v), where v is the number of vertices in the binary tree,
# and space complexity is O(v) (since worst case you're holding every vertex
# in the queue).
