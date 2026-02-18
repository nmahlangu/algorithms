from typing import *
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        if not times:
            return -1

        adj_list: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((v, w))

        heap: list[tuple[int, int]] = [(0, k)]
        distances: dict[int, int] = {k: 0}

        while heap:
            dist, node = heapq.heappop(heap)

            # visited check
            if dist > distances.get(node, float("inf")):
                continue

            for neighbor, weight in adj_list[node]:
                new_dist: int = dist + weight
                if new_dist < distances.get(neighbor, float("inf")):
                    distances[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor))

        return max(distances.values()) if len(distances) == n else -1
