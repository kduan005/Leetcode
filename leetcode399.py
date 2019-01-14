class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def doQuery(a, b):
            if a == b and a in g: return 1.0
            q = [(a, 1.0)]
            visited = set()
            while q:
                cur, val = q.pop(0)
                if cur not in g:
                    return -1.0
                else:
                    visited.add(cur)
                    for nei in g[cur]:
                        if nei not in visited:
                            if nei == b:
                                return val * g[cur][nei]
                            else:
                                q.append((nei, val * g[cur][nei]))
            return -1.0


        g = {}
        for i, (a, b) in enumerate(equations):
            if a in g:
                g[a][b] = values[i]
            else:
                g[a] = {b: values[i]}
            if b in g:
                g[b][a] = 1 / values[i]
            else:
                g[b] = {a: 1 / values[i]}
        res = []
        for query in queries:
            a, b = query
            res.append(doQuery(a, b))
        return res
                
