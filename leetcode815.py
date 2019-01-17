import collections
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T: return 0
        stop_bus = collections.defaultdict(set)
        for bus in range(len(routes)):
            for stop in routes[bus]:
                stop_bus[stop].add(bus)

        graph = collections.defaultdict(set)
        for buses in stop_bus.values():
            for b1, b2 in itertools.combinations(buses, 2):
                graph[b1].add(b2)
                graph[b2].add(b1)

        cur, target = stop_bus[S], stop_bus[T]
        visited, count = set(), 0
        while cur:
            count += 1
            tmp = set()
            visited |= cur
            for bus in cur:
                if bus in target:
                    return count
                else:
                    for nxt in graph[bus]:
                        if nxt not in visited:
                            tmp.add(nxt)
            cur = tmp
        return -1
                
