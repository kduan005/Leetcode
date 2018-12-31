class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def dfs(pref, res):
            if pref <= n:
                res.append(pref)
            if pref * 10 <= n:
                dfs(pref * 10, res)
            if pref % 10 < 9:
                if pref + 1 <= n:
                    dfs(pref + 1, res)

        res = []
        dfs(1, res)
        return res
        
