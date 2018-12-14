class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations: return 0
        n = len(citations)
        l, r = 0, n-1
        while l < r:
            mid = l + (r-l)/2
            if citations[mid] < n - mid:
                l = mid + 1
            else:
                r = mid
        if citations[l] >= n-l:
            return n-l
        else:
            return 0
        
