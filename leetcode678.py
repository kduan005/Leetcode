class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, wild = [], []
        for i in range(len(s)):
            if s[i] == "*":
                wild.append(i)
            elif s[i] == ")" and stack and s[stack[-1]] == "(":
                stack.pop()
            else:
                stack.append(i)
        if not stack: return True
        stack.extend(wild)
        stack.sort()
        stack2 = []
        for i in stack:
            if s[i] == ")" and stack2 and s[stack2[-1]] == "*":
                stack2.pop()
            elif s[i] == "*" and stack2 and s[stack2[-1]] == "(":
                stack2.pop()
            else:
                stack2.append(i)
        return not stack2 or all(s[i] == "*" for i in stack2)
