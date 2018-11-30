# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        preorder, inorder = [], []
        def helper(root):
            if not root:
                return
            preorder.append(root.val)
            helper(root.left)
            inorder.append(root.val)
            helper(root.right)
        helper(root)
        return ":".join(map(str, preorder)) + ":" + ":".join(map(str, inorder))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        l = data.split(":")
        if l == ["", ""]: return None
        preorder, inorder = map(int, l[:len(l)/2]), map(int, l[len(l)/2:])
        def helper(preorder, inorder):
            if not preorder: return None
            if len(preorder) == 1:
                return TreeNode(preorder[0])
            root = TreeNode(preorder[0])
            ind = inorder.index(root.val)
            left = helper(preorder[1:1+ind], inorder[:ind])
            right = helper(preorder[1+ind:], inorder[ind+1:])
            root.left = left
            root.right = right
            return root
        return helper(preorder, inorder)



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
