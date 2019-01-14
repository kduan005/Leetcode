class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def find(a):
            p = a
            while p != parent[p]:
                p = parent[p]
            while parent[a] != p:
                b = parent[a]
                parent[a] = p
                a = b
            return p

        N = len(edges)
        parent = [0] * (N+1)

        e1, e2 = [-1, -1], [-1, -1]
        for i, (father, child) in enumerate(edges):
            if parent[child] == 0:
                parent[child] = father
            else:
                e1 = [parent[child], child]
                e2 = [father, child]
                edges[i] = [0, 0]

        parent = [i for i in range(N+1)]
        for father, child in edges:
            if father == child == 0:
                continue
            if find(father) == find(child):
                if e1 == [-1, -1]:
                    return [father, child]
                else:
                    return e1
            parent[child] = father
        return e2                
