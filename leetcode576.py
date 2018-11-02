class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """

        def dfs(m, n, N, i, j, dic):
            if (i, j, N) in dic:
                return dic[(i, j, N)]
            if N == 0:
                if 0 <= i <= m-1 and 0 <= j <= n-1:
                    dic[(i, j, N)] = 0
                    return 0
            if i < 0 or i > m-1 or j < 0 or j > n-1:
                dic[(i, j, N)] = 1
                return 1
            count = 0
            for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                count += dfs(m, n, N-1, i + x, j + y, dic) % (10 ** 9 + 7)
                count %= (10 ** 9 + 7)
            dic[(i, j, N)] = count % (10 ** 9 + 7)
            return count % (10 ** 9 + 7)

        return dfs(m, n, N, i, j, {}) % (10 ** 9 + 7)
