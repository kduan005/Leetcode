class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for n in num:
            while stack and ord(stack[-1]) - ord("0") > ord(n) - ord("0") and k:
                stack.pop()
                k -= 1
            stack.append(n)
        while k:
            stack.pop()
            k -= 1
        if not stack:
            return "0"
        else:
            return str(int("".join(stack)))

                
