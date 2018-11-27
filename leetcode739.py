class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        res = [0 for i in range(len(T))]
        stack = []
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                tp = stack.pop()
                res[tp] = i - tp
            stack.append(i)
        for i in stack:
            res[i] = 0
        return res
        
