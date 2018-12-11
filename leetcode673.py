class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dp = [[1,1] for i in range(len(nums))]
        for i in range(1, len(nums)):
            length, count = 0, [1]
            for j in range(i):
                if nums[j] < nums[i] and dp[j][0] > length:
                    count = [dp[j][1]]
                    length = dp[j][0]
                elif nums[j] < nums[i] and dp[j][0] == length:
                    count.append(dp[j][1])
            dp[i] = [length+1, sum(count)]
        length, count = 1, []
        for i in range(len(nums)):
            if dp[i][0] > length:
                length, count = dp[i][0], [dp[i][1]]
            elif dp[i][0] == length:
                count.append(dp[i][1])
        return sum(count)
                
