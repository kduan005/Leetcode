class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 0
        def findn(cur, nxt, step, res):
            step += 1
            if cur + nxt == n:
                res.append(step)
                return
            elif cur + nxt < n:
                findn(cur+nxt, nxt, step, res)
                findn(cur+nxt, cur+nxt, step+1, res)
            else:
                return
        res = []
        findn(1, 1, 1, res)
        return min(res)
        
