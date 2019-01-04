class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dic = {")": "(", "]": "[", "}": "{"}
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if stack and stack[-1] == dic[ch]:
                    stack.pop()
                else:
                    return False
        return not stack
