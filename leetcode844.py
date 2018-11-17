class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def cleanstr(s):
            stack = []
            for ch in s:
                if ch == "#":
                    if stack:
                        stack.pop()
                    else:
                        continue
                else:
                    stack.append(ch)
            return stack
        return cleanstr(S) == cleanstr(T)
