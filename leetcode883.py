class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        p1, p2, p3 = 0, 0, 0
        trans = [[] for i in range(n)]
        for i in range(m):
            for j in range(n):
                trans[j].append(grid[i][j])
                if grid[i][j] != 0:
                    p3 += 1
        for row in trans:
            p1 += max(row)
        for row in grid:
            p2 += max(row)

        return p1 + p2 + p3
            
