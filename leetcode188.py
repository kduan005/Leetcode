class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if k >= n / 2:
            H, N = float('-inf'), 0
            for price in prices:
                H, N = max(H, N - price), max(N, H + price)
            return N
        H, N = [float('-inf') for i in range(k+1)], [0 for i in range(k+1)]
        for price in prices:
            for j in range(1, k+1):
                H[j], N[j] = max(H[j], N[j-1] - price), max(N[j], H[j] + price)
        return N[k]

            
