class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        def isConcatenated(word, dic):
            if not word or not dic: return False
            dp = [False for i in range(len(word)+1)]
            dp[0] = True
            for i in range(1, len(word)+1):
                for j in range(i):
                    dp[i] = dp[j] and (word[j:i] in dic)
                    if dp[i]:
                        break
            return dp[-1]

        words.sort(key = len)
        res = []
        dic = set()
        for i, word in enumerate(words):
            if isConcatenated(word, dic):
                res.append(word)
            dic.add(word)
        return res
        
