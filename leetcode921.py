class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for ch in S:
            if ch == ")" and stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(ch)
        return len(stack)
