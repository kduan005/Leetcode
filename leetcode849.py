class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        l = -1
        res = 0
        while l < len(seats):
            r = l + 1
            while r < len(seats) and not seats[r]:
                r += 1
            if l == -1 or r == len(seats):
                dist = r - l - 1
            else:
                dist = (r - l) / 2
            res = max(res, dist)
            l = r
        return res
        
