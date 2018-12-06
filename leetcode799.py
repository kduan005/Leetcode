class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        ans = [[poured]]
        flag = True if poured > 1 else False
        i = 1
        while flag and i-1 <= query_row:
            flag = False
            ans.append([0 for _ in range(i + 1)])
            for j in range(i):
                if ans[i-1][j] > 1:
                    w = (ans[i-1][j] - 1) * 1.0 / 2
                    ans[i-1][j] = 1
                    ans[i][j] += w
                    ans[i][j+1] += w
                    flag = True
            i += 1
        return ans[query_row][query_glass] if query_row <= len(ans) - 1 else 0
