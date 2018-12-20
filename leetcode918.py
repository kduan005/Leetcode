class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dpmin, dpmax = [0 for i in range(len(A))], [0 for i in range(len(A))]
        dpmin[0], dpmax[0] = A[0], A[0]
        minsub, maxsub = A[0], A[0]
        for i in range(1, len(A)):
            dpmin[i] = A[i] if dpmin[i-1] > 0 else dpmin[i-1] + A[i]
            minsub = min(minsub, dpmin[i])
            dpmax[i] = A[i] if dpmax[i-1] < 0 else dpmax[i-1] + A[i]
            maxsub = max(maxsub, dpmax[i])
        return maxsub if maxsub < 0 else max(maxsub, sum(A) - minsub)
