class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def findMax(i, nums):
            if not i: return []
            count = len(nums) - i
            stack = []
            for n in nums:
                while stack and stack[-1] < n and count:
                    stack.pop()
                    count -= 1
                stack.append(n)
            while stack and count:
                stack.pop()
                count -= 1
            return stack

        def isGreater(l1, i, l2, j):
            if not l1: return False
            if not l2: return True
            while i < len(l1) and j < len(l2) and l1[i] == l2[j]:
                i += 1
                j += 1
            return j == len(l2) or i < len(l1) and l1[i] > l2[j]

        def merge(l1, l2):
            if not l1: return l2
            if not l2: return l1
            l, i, j = [], 0, 0
            while i < len(l1) and j < len(l2):
                if isGreater(l1, i, l2, j):
                    l.append(l1[i])
                    i += 1
                else:
                    l.append(l2[j])
                    j += 1
            if i < len(l1): l += l1[i:]
            else: l += l2[j:]
            return l

        res = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            l1, l2 = findMax(i, nums1), findMax(k-i, nums2)
            cand = merge(l1, l2)
            res = cand if isGreater(cand, 0, res, 0) else res
        return res
