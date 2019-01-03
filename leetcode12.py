class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = []
        dic = {3: {1: "M"},
               2: {5: "D", 1: "C"},
               1: {5: "L", 1: "X"},
               0: {5: "V", 1: "I"}}
        h = num / 1000
        res.extend([dic[3][1]] * h)
        num -= 1000 * h
        for i in range(2, -1, -1):
            k = num / (10 ** i)
            m = k / 5; n = k % 5
            if n == 4:
                res.append(dic[i][1])
                if m == 1:
                    res.append(dic[i+1][1])
                elif m == 0:
                    res.append(dic[i][5])
            else:
                res.extend([dic[i][5]] * m + [dic[i][1] * n])
            num -= k * (10 ** i)
        return "".join(res)
                
