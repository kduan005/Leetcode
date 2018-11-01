#BFS
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = [root]

        while q:
            leftmost = q[0].val
            tmp = []
            for node in q:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            q = tmp

        return leftmost
#DFS
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        node = root
        level = 0
        leftmost = (root, level)
        while stack or node:
            while node:
                stack.append((node, level))
                if level > leftmost[1]:
                    leftmost = (node, level)
                node = node.left
                level += 1
            node, level = stack.pop()
            node = node.right
            level += 1
        return leftmost[0].val
