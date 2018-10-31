#BFS
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        q = [root]
        res = []
        while q:
            m = float('-inf')
            tmp = []
            for node in q:
                m = max(m, node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            res.append(m)
            q = tmp
        return res
#DFS
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        res = []
        stack = []
        node, level = root, 0
        while stack or node:
            while node:
                if level > len(res)-1:
                    res.append(node.val)
                else:
                    res[level] = max(res[level], node.val)
                stack.append((node, level))
                node = node.left
                level += 1
            node, level = stack.pop()
            node = node.right
            level += 1
        return res
