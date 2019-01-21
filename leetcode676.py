class Trie(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False

class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie()


    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            cur = self.root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = Trie()
                cur = cur.children[c]
            cur.isEnd = True

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        candidates = [word[:i] + '*' + word[i+1:] for i in range(len(word))]
        for cand in candidates:
            cur = [self.root]
            for i, c in enumerate(cand):
                if c != '*':
                    tmp = [node.children[c] for node in cur if c in node.children]
                else:
                    tmp = [node.children[key] for node in cur for key in node.children if key != word[i]]
                cur = tmp
                if not cur:
                    break
            for node in cur:
                if node.isEnd:
                    return True
        return False



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
