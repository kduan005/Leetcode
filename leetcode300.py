#O(n2) time using DP
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dp = [0 for i in range(len(nums))]
        dp[0] = 1
        for i in range(1, len(nums)):
            tmplen = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > tmplen:
                        tmplen = dp[j] + 1
            if tmplen:
                dp[i] = tmplen
            else:
                dp[i] = 1

        return max(dp)

#O(nlogn) time using binary search
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        tails = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > tails[-1]:
                tails.append(nums[i])
            else:
                l, r = 0, len(tails)
                while l < r:
                    mid = l + (r-l)/2
                    if tails[mid-1] < nums[i] <= tails[mid]:
                        break
                    elif nums[i] > tails[mid]:
                        l = mid+1
                    else:
                        r = mid
                tails[mid] = nums[i]
        return len(tails)
