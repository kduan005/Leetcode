class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        def dfs(i, j, k, prob, dic):
            if i < 0 or i >= N or j < 0 or j >= N:
                return 0
            if (i, j, k) in dic:
                return dic[(i, j, k)]
            if k == 0:
                return prob
            res = 0
            for x, y in ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, -1), (2, 1), (-2, 1), (-2, -1)):
                res += dfs(i+x, j+y, k-1, (1.0/8) * prob, dic)
            dic[(i, j, k)] = dic[(i, N-1-j, k)] = dic[(N-1-i, j, k)] = dic[(N-1-i, N-1-j, k)]\
            = dic[(j, i, k)] = dic[(N-1-j, i, k)] = dic[(j, N-1-i, k)] = dic[(N-1-j, N-1-i, k)] = res
            return res
        return dfs(r, c, K, 1, {})
            
