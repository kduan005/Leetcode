class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n: return 0
        cur = [n]
        l = [i**2 for i in range(1, int(n**0.5)+1)]
        count = 0
        while cur:
            tmp = []
            count += 1
            for num in cur:
                for perf in l:
                    if num == perf: return count
                    elif num < perf: break
                    else: tmp.append(num - perf)
            cur = tmp
