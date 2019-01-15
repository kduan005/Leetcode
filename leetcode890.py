class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def isPattern(w1, w2):
            dic, s = {}, set()
            for i in range(len(w1)):
                if w1[i] not in dic:
                    if w2[i] not in s:
                        dic[w1[i]] = w2[i]
                        s.add(w2[i])
                    else:
                        return False
                else:
                    if w2[i] != dic[w1[i]]:
                        return False
            return True
        res = []
        for word in words:
            if isPattern(word, pattern):
                res.append(word)
        return res
        
