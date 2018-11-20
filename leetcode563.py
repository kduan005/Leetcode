# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.result = 0
        self.dic = {}
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.getSum(root)
        return self.result

    def getSum(self, root):
        if not root:
            return 0
        if root in self.dic:
            return self.dic[root]
        left = self.getSum(root.left)
        right = self.getSum(root.right)
        self.result += abs(left - right)
        self.dic[root] = root.val + left + right
        return self.dic[root]
