import collections

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        def union(e1, e2, dic):
            r1, r2 = find(e1, dic), find(e2, dic)
            if r1 < r2:
                dic[r2] = r1
            else:
                dic[r1] = r2

        def find(e, dic):
            f = e
            while dic[f] != f:
                f = dic[f]
            while dic[e] != f:
                t = dic[e]
                dic[e] = f
                e = t
            return f

        namedic = {}
        emaildic = {}
        for entry in accounts:
            name = entry[0]
            emails = entry[1:]
            for email in emails:
                if email not in emaildic:
                    emaildic[email] = email
                namedic[email] = name
            for i in range(len(emails)-1):
                union(emails[i], emails[i+1], emaildic)
        for email in emaildic:
            find(email, emaildic)

        resdic = collections.defaultdict(list)
        for email, root in emaildic.items():
            resdic[root].append(email)
        res = []
        for root, emaillist in resdic.items():
            emaillist.sort()
            res.append([namedic[root]]+emaillist)
        return res
