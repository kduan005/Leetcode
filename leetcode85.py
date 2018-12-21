class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        res, h = 0, [0 for i in range(n)]
        for i in range(m):
            l, r, stack = [0 for k in range(n)], [0 for k in range(n)], []
            for j in range(n):
                h[j] = 0 if matrix[i][j] == "0" else h[j] + 1
                while stack and h[stack[-1]] >= h[j]:
                    r[stack.pop()] = j
                l[j] = -1 if not stack else stack[-1]
                stack.append(j)
            while stack:
                r[stack.pop()] = n
            rowmax = max([(r[k] - l[k] - 1) * h[k] for k in range(n)])
            res = max(res, rowmax)
        return res
            
