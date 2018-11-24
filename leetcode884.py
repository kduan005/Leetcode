import collections
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        l1, l2 = A.split(), B.split()
        dic = collections.Counter(l1 + l2)
        res = []
        for word in dic:
            if dic[word] == 1:
                res.append(word)
        return res
        
