import collections
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        q = []
        degree = [0 for i in range(len(graph))]
        innode = collections.defaultdict(list)
        for i in range(len(degree)):
            degree[i] = len(graph[i])
            if degree[i] == 0:
                q.append(i)
            for child in graph[i]:
                innode[child].append(i)

        for termnode in q:
            for parent in innode[termnode]:
                degree[parent] -= 1
                if degree[parent] == 0:
                    q.append(parent)

        return sorted(q)
            
