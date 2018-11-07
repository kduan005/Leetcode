#BFS
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        cur = [root]
        numset = set()
        while cur:
            tmp = []
            for node in cur:
                if k - node.val in numset:
                    return True
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
                numset.add(node.val)
            cur = tmp
        return False
#DFS
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        node = root
        stack = []
        dic = set()
        while node or stack:
            while node:
                if k - node.val in dic:
                    return True
                dic.add(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return False
