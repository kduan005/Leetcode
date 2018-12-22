class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        i, ans = 0, 0
        while i <= n - 1:
            lmin, lmax = arr[i], arr[i]
            for j in range(i+1, n+1):
                if lmin == i and lmax == j-1:
                    ans += 1
                    break
                lmin, lmax = min(lmin, arr[j]), max(lmax, arr[j])
            i = j
        return ans
        
