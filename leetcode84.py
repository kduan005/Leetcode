class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights: return 0
        left, right = [0 for i in range(len(heights))], [0 for i in range(len(heights))]
        stack, i = [], 0
        while i < len(heights):
            while stack and heights[stack[-1]] > heights[i]:
                right[stack.pop()] = i
            left[i] = stack[-1] if stack else -1
            stack.append(i)
            i += 1
        while stack:
            right[stack.pop()] = len(heights)
        return max([(right[i] - left[i] - 1) * heights[i] for i in range(len(heights))])
