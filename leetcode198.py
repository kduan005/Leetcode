class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dp = [0 for i in range(len(nums)+2)]
        dp[2] = nums[0]
        i = 3
        while i < len(nums)+2:
            dp[i] = max(dp[i-3] + nums[i-2], dp[i-2] + nums[i-2])
            i += 1
        return max(dp[-1], dp[-2])
