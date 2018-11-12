import collections
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = collections.defaultdict(int)
        for ch in s:
            dic[ch] += 1
        bucket = ["" for i in range(len(s)+1)]
        for ch, count in dic.items():
            bucket[count] += ch * count
        return "".join(bucket[::-1])
