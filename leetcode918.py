class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dpmin, dpmax = A[0], A[0]
        minsub, maxsub = A[0], A[0]
        for i in range(1, len(A)):
            dpmin = A[i] if dpmin > 0 else dpmin + A[i]
            minsub = min(minsub, dpmin)
            dpmax = A[i] if dpmax < 0 else dpmax + A[i]
            maxsub = max(maxsub, dpmax)
        return maxsub if maxsub < 0 else max(maxsub, sum(A) - minsub)
