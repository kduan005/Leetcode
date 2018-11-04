class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
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

        l = [0 for i in range(N)]
        graph = [[] for i in range(N)]
        for i, j in dislikes:
            graph[i-1].append(j-1)
            graph[j-1].append(i-1)
        for i in range(len(graph)):
            if not l[i] and not dfs(i, l, 1):
                return False
        return True


            
