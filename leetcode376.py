class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2: return n
        diff = [nums[i+1] - nums[i] for i in range(n-1)]
        dp = [0 for i in range(n-1)]
        dp[0] = 0 if not diff[0] else 1
        for i in range(1, n-1):
            if diff[i] * diff[i-1] < 0:
                dp[i] = dp[i-1] + 1
            elif diff[i] * diff[i-1] > 0:
                dp[i] = dp[i-1]
            elif diff[i] == 0:
                dp[i] = dp[i-1]
                diff[i] = diff[i-1]
            else:
                dp[i] = 1
        return dp[-1] + 1
