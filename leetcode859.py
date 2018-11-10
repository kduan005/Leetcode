class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        switch = None
        if A == B:
            for i in range(len(A)):
                if (A[i] in A[:i]) or (A[i] in A[i+1:]):
                    return True
        for i in range(len(A)):
            if A[i] != B[i]:
                if not switch:
                    switch = (A[i], B[i])
                elif (B[i], A[i]) != switch:
                        return False
                elif A[i+1:] != B[i+1:]:
                    return False
                else:
                    return True
        return False
