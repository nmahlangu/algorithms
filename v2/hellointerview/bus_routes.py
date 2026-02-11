from typing import *
from collections import deque
from collections import defaultdict

class Solution:
    def bus_routes(self, routes: List[List[int]], source: int, target: int):
        # bfs is across routes
        # create mapping of bus stop to route index
        # initialize bfs at source bus stop
        # bfs
        #   get all routes this bus stop is on
        #   for each route, loop through the bus stops and see if it matches target
        #   if it doesn't, get all neighboring routes you can go to from that bus stop
        #   put them in the queue and store you visited them
        if source == target:
            return 0

        bus_stop_to_route: defaultdict[int, list[int]] = defaultdict(list)
        for i, route in enumerate(routes):
            for _, stop in enumerate(route):
                bus_stop_to_route[stop].append(i)

        queue: deque[int] = deque(bus_stop_to_route[source]) # stores route index
        visited: set[int] = set(bus_stop_to_route[source]) # stores route indexes
        num_buses: int = 1

        while queue:
            for _ in range(len(queue)):
                route_idx: int = queue.popleft()
                for bus_stop in routes[route_idx]:
                    if bus_stop == target:
                        return num_buses

                    for neighbor_route_idx in bus_stop_to_route[bus_stop]:
                        if neighbor_route_idx not in visited:
                            visited.add(neighbor_route_idx)
                            queue.append(neighbor_route_idx)
            
            num_buses += 1

        return -1
