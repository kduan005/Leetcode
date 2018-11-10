import collections
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        if k < 0: return 0
        if k == 0:
            dic = collections.defaultdict(int)
            for num in nums:
                dic[num] += 1
            for _, n in dic.items():
                if n > 1:
                    count += 1
            return count
        visited = set()
        s = set(nums)
        for num in s:
            if num not in visited and num + k in s:
                count += 1
                visited.add(num)
        return count
        
