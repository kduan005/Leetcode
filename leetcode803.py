class Solution(object):
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        self.size = collections.defaultdict(lambda: 1)

        def find(t):
            while parent[t] != t:
                parent[t] = parent[parent[t]]
                t = parent[t]
            return t

        def union(a, b):
            parent.setdefault(a, a)
            parent.setdefault(b, b)
            pa, pb = find(a), find(b)
            if pa == pb:
                return
            else:
                if pa == (-1, -1):
                    parent[pb] = pa
                    self.size[pa] += self.size[pb]
                else:
                    parent[pa] = pb
                    self.size[pb] += self.size[pa]

        def unionAround(i, j):
            if i == 0:
                union((-1, -1), (i, j))
            for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                if 0 <= i+dx < m and 0 <= j+dy < n:
                    if grid[i+dx][j+dy] == 1:
                        union((i, j), (i+dx, j+dy))

        for hit in hits:
            if grid[hit[0]][hit[1]] == 1:
                grid[hit[0]][hit[1]] = 2

        parent = {}

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    unionAround(i, j)

        res, count = [], self.size[(-1, -1)]
        for hit in hits[::-1]:
            if grid[hit[0]][hit[1]] == 2:
                grid[hit[0]][hit[1]] = 1
                unionAround(hit[0], hit[1])
                res.append(self.size[(-1, -1)] - count - 1 if self.size[(-1, -1)] - count - 1 > 0 else 0)
                count = self.size[(-1, -1)]
            else:
                res.append(0)

        return res[::-1]
                
