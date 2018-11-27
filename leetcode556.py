class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10: return -1
        s = list(str(n)[::-1])
        stack = [0]
        for i in range(1,len(s)):
            if s[i] >= s[i-1]:
                stack.append(i)
            else:
                break
        if i == len(s)-1 and s[i] >= s[i-1]:
            return -1
        else:
            while stack and s[stack[-1]] > s[i]:
                tp = stack.pop()
        res = int("".join(sorted(s[:tp] + s[tp+1:i+1], reverse=True) + \
        [s[tp]] + s[i+1:])[::-1])        
        if res > 2147483647:
            return -1
        else:
            return res
