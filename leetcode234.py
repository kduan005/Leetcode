# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def reverse(head):
            cur = head
            tail = None
            while cur:
                nxt = cur.next
                cur.next = tail
                tail = cur
                cur = nxt
            return tail

        f, s = head, head
        while f and f.next:
            f = f.next.next
            s = s.next
        if f:
            s = s.next
        s, f = reverse(s), head
        while s:
            if s.val != f.val:
                return False
            s, f = s.next, f.next
        return True
