class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        n = len(A)
        dp = [[float('+inf') for j in range(n+2)] for i in range(n+1)]
        dp[0] = [0 for j in range(n+2)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]) + A[i-1][j-1]
        return min(dp[-1][1:-1])
        
