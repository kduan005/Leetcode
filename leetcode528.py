class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.range = []
        s = 0
        for num in w:
            s += num
            self.range.append(s)

    def pickIndex(self):
        """
        :rtype: int
        """
        d = random.randint(1, self.range[-1])
        l, r = 0, len(self.range)
        while l < r:
            mid = l + (r - l) / 2
            if self.range[mid] < d:
                l = mid + 1
            else:
                r = mid
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
