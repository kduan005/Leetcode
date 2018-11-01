class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        board = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    continue
                else:
                    visited = set()
                    self.findDist(i, j, matrix, board, visited, m, n)
        return board

    def findDist(self, i, j, matrix, board, visited, m, n):
        q = [(i, j)]
        dist = 0
        while q:
            tmp = []
            for node in q:
                for x, y in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                    if 0 <= node[0] + x <= m-1 and 0 <= node[1] + y <= n-1:
                        if matrix[node[0] + x][node[1] + y] == 0:
                            dist += 1
                            board[i][j] = dist
                            return
                        elif (node[0] + x, node[1] + y) not in visited:
                            tmp.append((node[0] + x, node[1] + y))
                            visited.add((node[0] + x, node[1] + y))
            dist += 1
            q = tmp
