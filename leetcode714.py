class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        if n <= 1: return 0
        H, NH = [0 for i in range(n)], [0 for i in range(n)]
        H[0], NH[0] = -prices[0], 0
        for i in range(1, n):
            H[i] = max(H[i-1], NH[i-1] - prices[i])
            NH[i] = max(NH[i-1], H[i-1] + prices[i] - fee)
        return max(H[-1], NH[-1])
        
