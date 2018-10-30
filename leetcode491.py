class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        #key here is to use a set to store all the sequences that have been seen
        #rather than looking sequences up in the list, or it will TLE otherwise.
        s = set()
        for num in nums:
            tmp = []
            if res:
                for pref in res:
                    if num >= pref[-1] and tuple(pref + [num]) not in s:
                        tmp.append(pref + [num])
                        s.add(tuple(pref + [num]))
                res.extend(tmp)
            if [num] not in res:
                res.append([num])
                s.add(tuple([num]))
        res_f = [seq for seq in res if len(seq) > 1]
        return res_f
