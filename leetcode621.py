import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        dic = collections.Counter(tasks)
        m = max(dic.values())
        res = (m-1) * (n+1)
        for val in dic.values():
            if val > m-1:
                res += val - (m-1)
        return max(res, len(tasks))
