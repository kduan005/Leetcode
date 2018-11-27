class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        res = 0
        for c in S:
            if c == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                    res -= 1
                else:
                    res += 1
            else:
                res += 1
                stack.append(c)
        return res
