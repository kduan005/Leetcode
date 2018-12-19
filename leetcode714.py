class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        H, N = float('-inf'), 0
        for price in prices:
            H, N = max(H, N - price), max(N, H + price - fee)
        return N
