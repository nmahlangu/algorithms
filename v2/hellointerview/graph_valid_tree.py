from typing import *
from collections import defaultdict


class Solution:
    def graph_valid_tree(self, n: int, edges: List[List[int]]):
        if not edges:
            return True

        adj_list: defaultdict[int, list[int]] = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited: set[int] = set()
        return self.has_cycle(
            node=edges[0][0], adj_list=adj_list, visited=visited, parent=-1
        )

    def has_cycle(
        self, node: int, adj_list: Dict[int, list[int]], visited: set[int], parent: int
    ) -> bool:
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor in visited and neighbor != parent:
                return True
            elif neighbor not in visited and self.has_cycle(
                neighbor=neighbor, adj_list=adj_list, visited=visited, parent=node
            ):
                return True
        return False
