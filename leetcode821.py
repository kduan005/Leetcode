class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        n = len(S)
        d1, d2 = [float('+inf') for i in range(n+1)], [float('+inf') for i in range(n+1)]
        for i in range(1, n+1):
            d1[i] = d1[i-1] + 1 if S[i-1] != C else 0
            d2[n-i] = d2[n-i+1] + 1 if S[n-i] != C else 0
        res = []
        for i in range(n):
            res.append(min(d1[i+1], d2[i]))
        return res

        
