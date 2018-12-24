class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = 0
        for num in nums:
            s ^= num
        lastbit = s & -s
        a, b = 0, 0
        for num in nums:
            if num & lastbit:
                a ^= num
            else:
                b ^= num
        return [a, b]
