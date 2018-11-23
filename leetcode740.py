import collections
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dic = collections.Counter(nums)
        m = max(dic)
        dp = [0 for i in range(m+1)]
        dp[1] = dic[1] * 1
        i = 2
        while i < m+1:
            dp[i] = max(dp[i-1], dp[i-2] + dic[i] * i)
            i += 1
        return dp[m]
