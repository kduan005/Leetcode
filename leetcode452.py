class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points: return 0
        points.sort(key = lambda p: p[1])
        i, count = 0, 1
        while i < len(points):
            j = i + 1
            while j < len(points):
                if points[i][1] >= points[j][0]:
                    j += 1
                else:
                    break
            if j != len(points):
                count += 1
            i = j
        return count
        
