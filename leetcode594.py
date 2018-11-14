import collections
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dic = collections.Counter(nums)
        length = 0
        for num in dic:
            if num-1 in dic:
                length = max(length, dic[num] + dic[num-1])
        return length
