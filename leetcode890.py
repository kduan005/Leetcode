import collections
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def isSame(w1, w2):
            dic, s, taken = {}, "", set()
            for i, ch in enumerate(w1):
                if ch in dic:
                    s += dic[ch]
                else:
                    if w2[i] not in taken:
                        s += w2[i]
                        dic[ch] = w2[i]
                        taken.add(w2[i])
                    else:
                        return False
            return s == w2
        res = []
        for word in words:
            if isSame(word, pattern):
                res.append(word)
        return res
                    
