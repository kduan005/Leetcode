class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        H, N, R = float('-inf'), 0, 0
        for price in prices:
            H, N, R = max(H, R - price), H + price, max(R, N)
        return max(R, N)
