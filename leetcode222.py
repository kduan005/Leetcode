# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(root):
            if not root: return 0
            count = 0
            while root:
                count += 1
                root = root.left
            return count
        if not root:
            return 0
        h = depth(root)
        if depth(root.right) == h-1:
            return 2 ** (h-1) + self.countNodes(root.right)
        else:
            return self.countNodes(root.left) + 2 ** (h-2)
