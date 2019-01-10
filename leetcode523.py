import collections
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if any(nums[i] == nums[i+1] == 0 for i in range(len(nums)-1)):
            return True
        if k == 0: return False
        dic = collections.defaultdict(int)
        s = 0
        dic[s] = -1
        for i, num in enumerate(nums):
            s += num
            mod = s % k
            if mod in dic and dic[mod] < i-1:
                return True
            if mod not in dic:
                dic[mod] = i
        return False
        
