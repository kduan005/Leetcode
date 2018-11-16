import heapq
class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        q, bound, dist, k, tail = [], [0, 0], float('+inf'), len(nums), float('-inf')
        for i in range(k):
            heapq.heappush(q, (nums[i][0], i))
            if tail < nums[i][0]:
                tail = nums[i][0]
            nums[i].pop(0)
        while True:
            head, j = heapq.heappop(q)
            if tail - head < dist:
                bound[0], bound[1] = head, tail
                dist = tail - head
            if not nums[j]:
                break
            heapq.heappush(q, (nums[j][0], j))
            if nums[j][0] > tail:
                tail = nums[j][0]
            nums[j].pop(0)
        return bound
            
