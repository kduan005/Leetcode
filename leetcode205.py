class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic, chset = {}, set()
        for i in range(len(s)):
            if s[i] not in dic and t[i] not in chset:
                dic[s[i]] = t[i]
                chset.add(t[i])
            elif s[i] in dic and dic[s[i]] == t[i]:
                continue
            elif s[i] not in dic and t[i] in chset:
                return False
            elif s[i] in dic and dic[s[i]] != t[i]:
                return False
        return True
        
