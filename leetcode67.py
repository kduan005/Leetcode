class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j, carry = len(a)-1, len(b)-1, 0
        res = ""
        while i >= 0 or j >= 0 or carry:
            n1 = n2 = 0
            if i >= 0:
                n1 = ord(a[i]) - ord('0')
            if j >= 0:
                n2 = ord(b[j]) - ord('0')
            res = str((n1 + n2 + carry) % 2) + res
            carry = (n1 + n2 + carry) / 2
            i -= 1
            j -= 1
        return res
