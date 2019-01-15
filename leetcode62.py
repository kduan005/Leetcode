class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for j in range(1, n+1):
            for i in range(1, m+1):
                if i == j == 1:
                    dp[1][1] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]
        
