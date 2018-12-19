class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        H, N = [float('-inf') for i in range(3)], [0 for i in range(3)]
        for price in prices:
            for k in range(1, 3):
                H[k], N[k] = max(H[k], N[k-1] - price), max(N[k], H[k] + price)
        return N[2]
