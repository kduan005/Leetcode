# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
import collections
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return node
        dic = collections.defaultdict(lambda: UndirectedGraphNode(0))
        q = [node]
        visited = set()
        while q:
            n = q.pop(0)
            if n.label not in visited:
                visited.add(n.label)
                dic[n].label = n.label
                for nei in n.neighbors:
                    if nei.label not in visited:
                        q.append(nei)
                    dic[n].neighbors.append(dic[nei])

        return dic[node]
