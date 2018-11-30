# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        def genCode(root, d):
            if not root:
                return "N"
            if root in d:
                return d[root]
            st = genCode(root.left, d) + str(root.val) + genCode(root.right, d) + str(root.val)
            d[root] = st
            return st
        if not root: return []
        q = [root]
        res, dic, d = [], defaultdict(int), {}
        while q:
            left, right = q[0].left, q[0].right
            for node in (left, right):
                if node:
                    q.append(node)
                    st = genCode(node, d)
                    dic[st] += 1
                    if dic[st] == 2:
                        res.append(node)
            q.pop(0)
        return res

        
