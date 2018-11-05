class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def leafSequence(root):
            node, stack, leaf = root, [], []
            while stack or node:
                while node:
                    stack.append(node)
                    if not node.left and not node.right:
                        leaf.append(node.val)
                    node = node.left
                node = stack.pop()
                node = node.right
            return leaf
        l1 = leafSequence(root1)
        l2 = leafSequence(root2)
        if l1 == l2:
            return True
        else:
            return False
