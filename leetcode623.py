# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            newroot = TreeNode(v)
            newroot.left = root
            return newroot
        cur = [(root, root.left, root.right)]
        depth = 1
        while True:
            if depth == d-1:
                break
            tmp = []
            for node, left, right in cur:
                if node.left:
                    tmp.append((node.left, node.left.left, node.left.right))
                if node.right:
                    tmp.append((node.right, node.right.left, node.right.right))
            cur = tmp
            depth += 1

        for node, left, right in cur:
            node.left = TreeNode(v)
            node.right = TreeNode(v)
            node.left.left = left
            node.right.right = right
        return root

        
