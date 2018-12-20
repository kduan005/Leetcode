import collections, bisect
#binary search
class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        dic = collections.defaultdict(list)
        for i, ch in enumerate(S):
            dic[ch].append(i)

        def isIn(word):
            prev = 0
            for ch in word:
                j = bisect.bisect_left(dic[ch], prev)
                if j == len(dic[ch]): return False
                prev = dic[ch][j] + 1
            return True

        ans = 0
        for word in words:
            if isIn(word): ans += 1
        return ans
#n pointer
class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        dic = collections.defaultdict(list)
        ans = 0
        for word in words:
            dic[word[0]].append(word[1:])
        ans = 0
        for ch in S:
            for rest in dic.pop(ch, ()):
                if not rest: ans += 1
                else:
                    dic[rest[0]].append(rest[1:])
        return ans
