class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def justify(words, spaces):
            n = len(words) - 1
            if not n:
                return words[0] + spaces * " "
            mod = spaces % n
            ceil = (spaces + n - 1)/n
            floor = spaces/n
            for i in range(mod):
                words.insert(2 * i + 1, ceil * " ")
            for j in range(mod, n):
                words.insert(2 * j + 1, floor * " ")
            return "".join(words)
        i = 0
        res = []
        while i < len(words):
            j = i
            count = 0
            line = []
            while j < len(words) and count + len(words[j]) + j - i <= maxWidth:
                line.append(words[j])
                count += len(words[j])
                j += 1
            if j == len(words):
                s = " ".join(line)
                res.append(s + (maxWidth - len(s)) * " ")
            else:
                res.append(justify(line, maxWidth - count))
            i = j
        return res if res else[" " * (maxWidth + 1)]
        
