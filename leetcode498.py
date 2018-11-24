class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        def printDiagonal(a, b, down):
            if down:
                while a <= m-1 and b >= 0:
                    res.append(matrix[a][b])
                    a += 1
                    b -= 1
                if b == -1 and not a == m: b = 0
                else:
                    a, b = m-1, b+2
            else:
                while a >=0 and b <= n-1:
                    res.append(matrix[a][b])
                    a -= 1
                    b += 1
                if a == -1 and not b == n:
                    a = 0
                else:
                    a, b = a+2, n-1
            return a, b, down ^ 1
        a, b, down, res = 0, 0, 0, []
        while not (a == m-1 and b == n-1):
            newa, newb, newdown = printDiagonal(a, b, down)
            a, b, down = newa, newb, newdown
        res.append(matrix[-1][-1])
        return res
