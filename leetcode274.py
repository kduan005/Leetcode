class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse = True)
        k = 0
        while citations:
            k += 1
            low = citations.pop(0)
            if low < k:
                return k-1
        return k
            
