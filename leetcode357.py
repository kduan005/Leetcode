class Solution(object):

    def __init__(self):
        self.dp = [1 for i in range(11)]
        self.dp[1] = 9
        for i in range(2, 11):
            self.dp[i] = self.dp[i-1] * (11-i)
        for i in range(1, 11):
            self.dp[i] += self.dp[i-1]

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.dp[n]
