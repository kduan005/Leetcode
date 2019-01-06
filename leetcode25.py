# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(node):
            tail = None
            cur = node
            while cur:
                nxt = cur.next
                cur.next = tail
                tail = cur
                cur = nxt

        dum = ListNode(-1)
        dum.next = head
        pre, end = dum, dum
        while True:
            i = 0
            while i < k and end.next:
                end = end.next
                i += 1
            if i < k:
                break
            prenxt, endnxt = pre.next, end.next
            end.next = None
            reverse(prenxt)
            pre.next, prenxt.next = end, endnxt
            pre, end = prenxt, prenxt
        return dum.next
