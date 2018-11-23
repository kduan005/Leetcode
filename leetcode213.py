class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        dp0 = [0 for i in range(len(nums)+1)]
        dp1 = [0 for i in range(len(nums)+1)]
        dp0[2], dp1[2] = nums[0], nums[1]
        i = 3
        while i < len(nums)+1:
            dp0[i] = max(dp0[i-3] + nums[i-2], dp0[i-2] + nums[i-2])
            dp1[i] = max(dp1[i-3] + nums[i-1], dp1[i-2] + nums[i-1])
            i += 1
        return max(dp0[-1], dp0[-2], dp1[-1], dp1[-2])
