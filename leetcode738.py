class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = str(N)
        n = len(s)
        stack, tp = [], None
        for i, num in enumerate(s):
            if (stack and ord(stack[-1][0]) - ord('0') > ord(num) - ord('0')):
                tp = stack.pop()
                while stack and tp[0] == stack[-1][0]:
                    tp = stack.pop()
                break
            else:
                stack.append((num, i))
        if tp:
            return int(str(''.join([num[0] for num in stack]) + str(int(tp[0])-1)) + '9' * (n-tp[1]-1))
        else:
            return N
