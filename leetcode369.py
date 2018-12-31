class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        s, f = sum(A), sum(A[i] * i for i in range(n))
        res = f
        for i in range(n-1):
            f += A[i] * n - s
            res = max(res, f)
        return res
