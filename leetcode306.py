class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def dfs(s, h, i, j, k):
            if int(s[h:i]) + int(s[i:j]) == int(s[j:k]):
                if k == len(s):
                    return True
                else:
                    for l in range(k+1, len(s)+1):
                        if l == k+1 or l > k+1 and s[k] != "0":
                            if dfs(s, i, j, k, l):
                                return True
            return False
        for i in range(1, len(num)-1):
            if i == 1 or i > 1 and num[0] != "0":
                for j in range(i+1, len(num)):
                    if j == i + 1 or j > i + 1 and num[i] != "0":
                        for k in range(j+1, len(num)+1):
                            if k == j + 1 or k > j + 1 and num[j] != "0":
                                if dfs(num, 0, i, j, k):
                                    return True
        return False
