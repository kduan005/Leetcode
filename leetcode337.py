# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def bestRob(root, dic):
            if not root:
                return 0
            if root in dic:
                return dic[root]
            amt = root.val
            if root.left:
                amt += bestRob(root.left.left, dic) + bestRob(root.left.right, dic)
            if root.right:
                amt += bestRob(root.right.left, dic) + bestRob(root.right.right, dic)
            amt = max(amt, bestRob(root.left, dic) + bestRob(root.right, dic))
            dic[root] = amt
            return amt

        return bestRob(root, {})
