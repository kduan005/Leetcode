# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists: return None

        if len(lists) == 1:
            return lists[0]

        newlists = []
        for i in range(len(lists)/2):
            newnode = self.mergeTwo(lists[2*i], lists[2*i+1])
            newlists.append(newnode)

        if len(lists) % 2 == 1:
            newlists.append(lists[-1])

        return self.mergeKLists(newlists)


    def mergeTwo(self, l1, l2):
            dum = ListNode(0)
            cur = dum
            if not l1:
                return l2
            if not l2:
                return l1
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            if l1:
                cur.next = l1
            if l2:
                cur.next = l2
            return dum.next
