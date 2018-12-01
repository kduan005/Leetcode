import collections
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        dic = collections.defaultdict(list)
        for trp in allowed:
            dic[trp[:2]].append(trp[2:])

        def dfs(cur, i, j):
            if i == j == 1:
                return True
            if i == j:
                i = 0
                j -= 1
            x = cur[i]
            for b in dic[cur[i] + cur[i+1]]:
                cur[i] = b
                if dfs(cur, i+1, j):
                    return True
                cur[i] = x
            return False

        cur = list(bottom)
        return dfs(cur, 0, len(cur)-1)
    
