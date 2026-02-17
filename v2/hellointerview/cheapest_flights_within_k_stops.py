from typing import *
import heapq
from collections import defaultdict

"""
A travel booking system needs to find the lowest-cost route between airports. You're given n cities connected 
by flights, where each flight [from, to, price] represents a direct route with its cost.

Find the cheapest route from src to dst that uses at most k layovers (intermediate cities). If no such route 
exists, return -1.

Note: A route with k layovers means visiting k intermediate cities, or equivalently, taking k+1 flights.
"""


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        if not flights:
            return -1

        # u: (v, w)
        adj_list: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
        for u, v, w in flights:
            adj_list[u].append((v, w))

        # (city, stops)
        best: dict[tuple[int, int], int] = {}

        # (cost, city, stops)
        heap: list[tuple[int, int, int]] = [(0, src, 0)]

        while heap:
            cost, city, stops = heapq.heappop(heap)

            if city == dst:
                return cost

            # too may layovers in path
            if stops > k:
                continue

            # found a cheaper path previously
            if (city, stops) in best and cost > best[(city, stops)]:
                continue

            best[(city, stops)] = cost

            for neighbor, weight in adj_list[city]:
                new_cost: int = cost + weight
                heapq.heappush(heap, (new_cost, neighbor, stops + 1))

        return -1
