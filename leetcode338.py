class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if not num: return [0]
        res = [0]
        while 2 * len(res) <= num + 1:
            tmp = [count+1 for count in res]
            res += tmp
        d = num + 1 - len(res)
        for i in range(d):
            res.append(res[i] + 1)
        return res
