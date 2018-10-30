# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.max = float('-inf')

        def traverse(root):
            if not root:
                return 0

            left = traverse(root.left)
            right = traverse(root.right)
            s_single = max(max(left, right) + root.val, root.val)
            s_double = max(s_single, root.val + left + right)
            self.max = max(self.max, s_double)

            return s_single

        traverse(root)

        return self.max
