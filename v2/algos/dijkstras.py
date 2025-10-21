import collections
import heapq
from typing import List, Tuple


class Dijkstras:
    """
    edges_and_weights: list of tuples in the form (source, destination, weight)
    n: number of nodes
    k: starting node

    Returns the sum of the weights of the shortest path from the starting node to all other nodes, or -1 if there is no path.
    """

    def get_shortest_path(
        self, edges_and_weights: List[Tuple[int, int, int]], n: int, k: int
    ) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in edges_and_weights:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1
