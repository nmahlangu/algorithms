
from Queue import PriorityQueue

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def djikstra(start,end,edge_weight):

    path_weight = {node: float('inf') if node != start else 0 for node in adj_list}
    previous    = {node: None for node in adj_list}
    pqueue      = PriorityQueue()
    pqueue.put((0,start))

    while not pqueue.empty():
        node = pqueue.pop()[1]
        for child in node.children:
            if path_weight[node] + edge_weight[(node,child)] < path_weight[child]:
                path_weight[child] = path_weight[node] + edge_weight[(node,child)]
                # TODO update pqueue path_weight of child
                try:
                    pqueue.get(child)
                except:
                    # do nothing
                pqueue.put((path_weight[child],child))
                previous[child] = node

    # TODO: retrace path from end to start (if possible)
