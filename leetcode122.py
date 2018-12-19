class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        H, N = float('-inf'), 0
        for price in prices:
            H, N = max(H, N - price), max(N, H + price)
        return N
