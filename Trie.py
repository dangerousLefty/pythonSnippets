
class TrieNode:
    def __init__(self):
        self.children = {}  # hashMap
        self.endOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return false
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return false
            cur = cur.children[c]
        return True


myTrie = Trie()

myTrie.insert("apple")
myTrie.insert("ape")
myTrie.insert("apathy")

myTrie.insert("flour")
myTrie.insert("flower")

myTrie.search("flow")
myTrie.startsWith("flow")
