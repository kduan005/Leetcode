class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        n = len(deck)
        res = [None for i in range(n)]
        i, count, flag = -1, 0, -1
        while count < n:
            i += 1
            if i == n: i = 0
            if res[i] != None: continue
            else: flag *= -1
            if flag == 1:
                res[i] = deck[count]
                count += 1
        return res
