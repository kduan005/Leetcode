class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp1, dp2 = [0 for j in range(len(s2)+1)], [0 for j in range(len(s2)+1)]
        for j in range(1, len(s2)+1):
            dp2[j] = dp2[j-1] + ord(s2[j-1])
        for i in range(1, len(s1)+1):
            dp1 = dp2[:]
            dp2 = [0 for j in range(len(s2)+1)]
            dp2[0] = dp1[0] + ord(s1[i-1])
            for j in range(1, len(s2)+1):
                if s1[i-1] != s2[j-1]:
                    dp2[j] = min(dp2[j-1] + ord(s2[j-1]), dp1[j] + ord(s1[i-1]))
                else:
                    dp2[j] = dp1[j-1]
        return dp2[-1]
