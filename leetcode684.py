class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def Find(a):
            p = a
            while p != parent[p]:
                p = parent[p]
            while parent[a] != p:
                b = parent[a]
                parent[a] = p
                a = b
            return p

        def Union(a, b):
            p1, p2 = Find(a), Find(b)
            if p1 == p2:
                return False
            else:
                if p1 < p2:
                    parent[p2] = p1
                else:
                    parent[p1] = p2
            return True

        N = len(edges)
        parent = [i for i in range(N+1)]
        for a, b in edges:
            if not Union(a, b):
                return [a, b]
            else:
                Union(a, b)
