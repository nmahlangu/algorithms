# Print a tree in level order

class Node:
    def __init__(self,n,children=[]):
        self.num = n
        self.children = children

def PrintTreeLevelByLevel(node):
    q = [node,'-']
    while q:
        elt = q.pop(0)
        if elt != '-':
            for c in elt.children:
                q.append(c)
            print elt.num,        
        else:
            print
            if len(q) == 0:
                break
            else:
                q.append("-")

# Perform BFS, keeping a dummy element in the queue of nodes to visit. Whenever the dummy
# is dequeued, print a newline and place the dummy back at the end of the queue (unless it's
# empty meaning there are no more nodes to visit and the traversal is done). For all other
# elements that are dequeued, enqueue all of it's children and print the parent (withou
# a newline).  
