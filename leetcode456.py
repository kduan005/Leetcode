class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mid, stack = float('-inf'), []
        for num in nums[::-1]:
            if mid and num < mid: return True
            while stack and stack[-1] < num:
                mid = max(mid, stack.pop())
            stack.append(num)
        return False
