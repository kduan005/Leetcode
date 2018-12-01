import collections
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        def mutable(s1, s2):
            count = 0
            for i in range(8):
                if s1[i] != s2[i]:
                    count += 1
            return count == 1
        dic = collections.defaultdict(list)
        bank.append(start)
        for i in range(len(bank)-1):
            for j in range(i, len(bank)):
                if mutable(bank[i], bank[j]):
                    dic[bank[i]].append(bank[j])
                    dic[bank[j]].append(bank[i])
        cur = [start]
        count = 0
        seen = set(cur)
        while cur:
            tmp = []
            for seq in cur:
                if seq == end:
                    return count
                else:
                    for nei in dic[seq]:
                        if nei not in seen:
                            tmp.append(nei)
                            seen.add(nei)
            cur = tmp
            count += 1
        return -1
        
