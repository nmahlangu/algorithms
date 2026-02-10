from typing import Dict, List


class IntGraphNode:
    def __init__(self, value, id, neighbors):
        self.value = value
        self.id = id
        self.neighbors = neighbors


class Solution:
    def copy_graph(self, node: IntGraphNode) -> Dict[int, List[int]]:
        if not node:
            return {}

        adj_list: Dict[int, List[int]] = {}
        self.copy_graph_helper(node=node, adj_list=adj_list)
        return adj_list

    def copy_graph_helper(self, node: IntGraphNode, adj_list: Dict[int, List[int]]):
        if node.value in adj_list:
            return

        adj_list[node.value] = [n.value for n in node.neighbors]
        for neighbor in node.neighbors:
            self.copy_graph_helper(node=neighbor, adj_list=adj_list)
        return
