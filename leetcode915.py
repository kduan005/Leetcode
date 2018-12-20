class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        B, m = [0 for i in range(len(A))], float('+inf')
        for i in range(len(A)-1, -1, -1):
            m = min(m, A[i])
            B[i] = m
        m = float('-inf')
        for i in range(len(A)-1):
            m = max(m, A[i])
            if m <= B[i+1]: return i+1
