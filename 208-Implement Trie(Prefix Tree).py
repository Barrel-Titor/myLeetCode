"""
https://leetcode.com/problems/implement-trie-prefix-tree/solution/
"""


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current = self.root
        for ch in word:
            current = current.setdefault(ch, {})
        current['$'] = '$'
        # print('print root:', self.root)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current = self.root
        for ch in word:
            if not current.get(ch):
                return False
            current = current.get(ch)
        if current.get('$'):
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current = self.root
        for ch in prefix:
            if not current.get(ch):
                return False
            current = current.get(ch)
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))    # return True
    print(trie.search("app"))      # return False
    print(trie.startsWith("app"))  # return True
    trie.insert("app")
    print(trie.search("app"))      # return True
