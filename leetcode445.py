# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        l, carry = None, 0
        while s1 or s2 or carry:
            newl = ListNode(0)
            val1 = s1.pop() if s1 else 0
            val2 = s2.pop() if s2 else 0
            newl.val = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) / 10
            newl.next = l
            l = newl
        return l
            
