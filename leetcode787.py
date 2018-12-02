#BFS
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        graph = [{} for i in range(n)]
        for i, j, price in flights:
            graph[i][j] = price
        l = [float('+inf') if i != src else 0 for i in range(n)]
        cur = [src]
        while K+1 and cur:
            tp = tuple(l)
            tmp = []
            for node in cur:
                for nei in graph[node]:
                    if tp[node] + graph[node][nei] < l[nei]:
                        l[nei] = tp[node] + graph[node][nei]
                        tmp.append(nei)
            cur = tmp
            K -= 1
        return l[dst] if l[dst] != float('+inf') else -1
#Since we've already know the length shortest path is no more than K, we could\
#solve this with Bellman-Ford
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        l = [float('+inf') if i != src else 0 for i in range(n)]
        while K+1:
            tp = tuple(l)
            for i, j, price in flights:
                l[j] = min(l[j], tp[i] + price)
            K -= 1
        return l[dst] if l[dst] != float('+inf') else -1
