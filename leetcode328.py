# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next: return head
        tail, prev, cur, i = head, head.next, head.next.next, 3
        while cur:
            if i % 2 == 1:
                cnxt, tnxt = cur.next, tail.next
                tail.next = cur
                cur.next = tnxt
                prev.next = cnxt
                tail = cur
                cur = cnxt
            else:
                prev = prev.next
                cur = cur.next
            i += 1

        return head
