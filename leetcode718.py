class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[0 for i in range(len(A)+1)] for j in range(len(B)+1)]
        for j in range(1, len(B)+1):
            for i in range(1, len(A)+1):
                if B[j-1] == A[i-1]:
                    dp[j][i] = dp[j-1][i-1]+1
        return max(max(dp[i]) for i in range(1, len(B)+1))
