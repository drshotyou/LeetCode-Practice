class Solution:
    def numBusesToDestination(self,routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0

        graph = {}
        for routed_id, stops in enumerate(routes):
            for stop in stops:
                if stop not in graph:
                    graph[stop] = set()
                graph[stop].add(stop)
        
        seen_routes = set()
        seen_stops = set([source])

        queue = deque([(source,0)])

        while queue:
            stop, numChanges = queue.popleft()
            if stop == destination:
                return numChanges
            for route_id in graph[stop]:
                if route_id not in seen_routes:
                    seen_routes.add(route_id)
                    for stop in routes[route_id]:
                        if stop not in seen_stops:
                            seen_stops.add(stop)
                            queue.append((stop,numChanges+1))
        return -1
