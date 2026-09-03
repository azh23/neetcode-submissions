class Node:
    def __init__(self, ch):
        self.ch = ch
        self.branch = [None for _ in range(27)]
class PrefixTree:
    def __init__(self):
        self.head = Node("$")
        
    def idx(self, ch: str) -> int:
        return ord(ch) - ord('a') + 1
    
    def process(self, word: str) -> int:
        curr = self.head
        ch_idx = 0
        while ch_idx < len(word) and curr.branch[self.idx(word[ch_idx])] is not None:
            curr = curr.branch[self.idx(word[ch_idx])]
            ch_idx += 1
        return curr, ch_idx

    def insert(self, word: str) -> None:
        curr, ch_idx = self.process(word)

        if ch_idx == len(word):
            if curr.branch[0] is None:
                curr.branch[0] = Node("$")
            return

        for i in range(ch_idx, len(word)):
            curr.branch[self.idx(word[i])] = Node(word[i])
            curr = curr.branch[self.idx(word[i])]

        curr.branch[0] = Node("$")


    def search(self, word: str) -> bool:
        curr, ch_idx = self.process(word)

        return ch_idx == len(word) and curr.branch[0] is not None

    def startsWith(self, prefix: str) -> bool:
        curr, ch_idx = self.process(prefix)

        return ch_idx == len(prefix)       