"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        stack = []
        node = head
        q = []
        while stack or node:
            while node:
                stack.append(node)
                q.append(node)
                if node.child:
                    tmp = node.child
                    node.child = None
                    node = tmp
                else:
                    tmp = node.next
                    node.next = None
                    node = tmp
            node = stack.pop()
            node = node.next
        q.append(None)
        for i in range(len(q)-1):
            q[i].next = q[i+1]
            if i > 0:
                q[i].prev = q[i-1]
        return q[0]

        
