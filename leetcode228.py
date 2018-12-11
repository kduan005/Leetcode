class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return []
        res = [[nums[0]]]
        for num in nums[1:]:
            if num == res[-1][-1] + 1:
                res[-1].append(num)
            else:
                res.append([num])
        res = [str(range[0]) + "->" + str(range[-1]) if len(range) > 1 \
               else str(range[0]) for range in res]
        return res
