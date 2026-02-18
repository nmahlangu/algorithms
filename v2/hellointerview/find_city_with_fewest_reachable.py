from typing import *

"""
A regional planning committee wants to identify the most "isolated" city in a road network. 
Given n cities connected by bidirectional roads with varying distances, find the city that 
can reach the fewest other cities within a given distance threshold.

If multiple cities have the same minimum count, return the city with the highest number.

Note: The distance between two cities is the shortest path distance considering all possible routes.
"""


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        # make graph of weights (start at negative infinity)
        # 3 loops to iterate over graph and update weights
        # iterate through each city and count how many other cities it can reach
        # given the distance threshold
        # return min of those

        # (i,j) = distance from vertex i to j, default to infinity (aka unreachable)
        dist: list[list[float]] = [
            [float("inf") for _ in range(n)] for _ in range(n)
        ]

        # store actual distances
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        # distance to self is 0
        for i in range(n):
            dist[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    intermed_dist: float = dist[i][k] + dist[k][j]
                    if intermed_dist < dist[i][j]:
                        dist[i][j] = intermed_dist

        min_reachable: int = n
        min_city: int = 0

        for city in range(n):
            num_reachable: int = len(
                [
                    1
                    for j in range(n)
                    if j != city and dist[city][j] <= distanceThreshold
                ]
            )
            if num_reachable <= min_reachable:
                min_reachable = num_reachable
                min_city = city

        return min_city
