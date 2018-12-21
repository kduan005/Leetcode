class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left, right = [0 for i in range(len(A))], [0 for i in range(len(A))]
        stack, i, ans = [], 0, 0
        while i < len(A):
            while stack and A[stack[-1]] >= A[i]:
                right[stack.pop()] = i
            left[i] = stack[-1] if stack else -1
            stack.append(i)
            i += 1
        while stack:
            right[stack.pop()] = len(A)
        for i in range(len(A)):
            ans += (i - left[i]) * (right[i] - i) * A[i]
            ans %= 10 ** 9 + 7
        return ans
