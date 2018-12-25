class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(30, -1, -1):
            cnt0, cnt1 = 0, 0
            for num in nums:
                if (num >> i) & 1:
                    cnt1 += 1
                else:
                    cnt0 += 1
            res += cnt0 * cnt1
        return res
                
