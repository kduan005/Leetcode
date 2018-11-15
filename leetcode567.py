class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1): return False
        target, window = [0 for i in range(26)], [0 for i in range(26)]
        for ch in s1:
            target[ord(ch) - ord('a')] += 1
        for i in range(len(s1)):
            window[ord(s2[i]) - ord('a')] += 1
        if target == window:
            return True
        for i in range(len(s1), len(s2)):
            window[ord(s2[i]) - ord('a')] += 1
            window[ord(s2[i - len(s1)]) - ord('a')] -= 1
            if window == target:
                return True
        return False

        
