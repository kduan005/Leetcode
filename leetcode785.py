class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        def dfs(node, l, group):
            if l[node]:
                if l[node] != group:
                    return False
                else:
                    return True
            else:
                l[node] = group
                for nei in graph[node]:
                    if not dfs(nei, l, group * -1):
                        return False
                return True

        l = [0 for i in range(len(graph))]
        for i in range(len(graph)):
            if not l[i] and not dfs(i, l, 1):
                return False
        return True
