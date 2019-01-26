class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        def BST(l, r, memo):
            if l == r:
                return 1
            if (l, r) in memo:
                return memo[(l, r)]
            res = 0
            for i in range(l, r):
                res += BST(l, i, memo) * BST(i+1, r, memo)
            memo[(l, r)] = res
            return res

        return BST(0, n, {})
        
