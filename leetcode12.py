class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = {3: {1: "M", 5:""},
               2: {1: "C", 5: "D"},
               1: {1: "X", 5: "L"},
               0: {1: "I", 5: "V"}}
        s = ""
        for k in range(3, -1, -1):
            d = num / (10 ** k)
            if d == 9:
                s += dic[k][1] + dic[k+1][1]
            elif d == 4:
                s += dic[k][1] + dic[k][5]
            else:
                s += dic[k][5] * (d/5) + dic[k][1] * (d - d/5 * 5)
            num %= (10 ** k)
        return s
