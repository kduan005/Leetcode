# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
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

        dum = ListNode(0)
        dum.next = head
        count, node = 0, dum
        while True:
            if count == m-1:
                preh = node
            if count == m:
                h = node
            if count == n:
                t = node
            if count == n+1:
                tnxt = node
                break
            node = node.next
            count += 1
        t.next = None
        reverse(h)
        preh.next, h.next = t, tnxt
        return dum.next
