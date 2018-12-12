# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root: return
        node, stack, inord, preord = root, [], [], []
        while node or stack:
            while node:
                stack.append(node)
                preord.append(node)
                node = node.left
            node = stack.pop()
            inord.append(node)
            node = node.right
        in_i, in_j = min(inord.index(p), inord.index(q)), max(inord.index(p), inord.index(q))
        pre_i, pre_j = min(preord.index(p), preord.index(q)), max(preord.index(p), preord.index(q))
        lca = None
        for node in inord[in_i+1:in_j]:
            k = preord.index(node)
            if k < pre_i and k < pre_j:
                lca = node
        return lca if lca else preord[pre_i]
