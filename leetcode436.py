# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        dic = {}
        for i, itv in enumerate(intervals):
            dic[itv] = i
        srt = sorted(intervals, key = lambda s: s.start)
        res = []
        for itv in intervals:
            l, r = 0, len(intervals)-1
            while l <= r:
                mid = (l + r) >> 1
                if srt[mid].start < itv.end:
                    l = mid + 1
                else:
                    r = mid - 1
            res.append(-1) if l == len(intervals) else res.append(dic[srt[l]])
        return res
