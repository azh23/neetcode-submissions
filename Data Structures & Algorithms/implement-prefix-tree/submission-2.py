from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.trie = TrieNode() 

    def process(self, word) -> TrieNode | None:
        curr = self.trie
        for ch in word:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return None
        return curr

    def insert(self, word: str) -> None:
        curr = self.trie
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True

    def search(self, word: str) -> bool:
        node = self.process(word)
        return bool(node) and node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.process(prefix)
        return bool(node)
        
        