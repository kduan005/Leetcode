class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.dic = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        if key in self.dic:
            val -= self.dic[key]
        else:
            self.dic[key] = val

        tmp = self.trie
        for ch in key:
            if ch in tmp:
                tmp[ch][0] += val
                tmp = tmp[ch][1]
            else:
                tmp[ch] = [val, {}]
                tmp = tmp[ch][1]

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        tmp = self.trie
        for ch in prefix:
            if ch not in tmp:
                return 0
            else:
                cnt = tmp[ch][0]
                tmp = tmp[ch][1]
        return cnt


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
