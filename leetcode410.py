class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def canSplit(s):
            count, cur = 1, 0
            for num in nums:
                if num > s:
                    return False
                if cur + num <= s:
                    cur += num
                else:
                    cur = num
                    count += 1
            return count <= m

        l, r = 0, sum(nums) + 1
        while l < r:
            mid = l + (r-l) / 2
            if canSplit(mid):
                r = mid
            else:
                l = mid + 1
        return l
