class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        s1, s2 = set(), set()
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                s2.add(stack.pop())
            stack.append(i)
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                s1.add(i)
            stack.append(i)
        return s1 & s2 != set()
