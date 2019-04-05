class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.range = []
        s = 0
        for num in w:
            s += num
            self.range.append(s)

    def pickIndex(self):
        """
        :rtype: int
        """
        d = random.randint(1, self.range[-1])
        l, r = 0, len(self.range)
        while l < r:
            mid = l + (r - l) / 2
            if self.range[mid] < d:
                l = mid + 1
            else:
                r = mid
        return l

class MorrisTraversal(object):
    def morrisTraversal(self, root):
        cur = root
        while cur:
            if not cur.left:
                print cur.val
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    print cur.val
                    cur = cur.right



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
