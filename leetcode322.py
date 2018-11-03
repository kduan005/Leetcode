class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('+inf') for i in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin])
            dp[i] += 1
        if dp[-1] != float('+inf'):
            return dp[-1]
        else:
            return -1
                
