from collections import deque

class WordDictionary:

    def __init__(self):
        self.tree = dict()

    def addWord(self, word: str) -> None:
        branch = self.tree
        
        for ch in word:
            if ch not in branch:
                branch[ch] = dict()
            branch = branch[ch]
        branch["$"] = dict()

    def search(self, word: str) -> bool:
        trees = deque()
        trees.append((self.tree,0))

        while trees:
            curr, ch_idx = trees.pop()

            if ch_idx == len(word):
                if "$" in curr:
                    return True
                continue

            ch = word[ch_idx]
            if ch == ".":
                for value in curr.values():
                    trees.append((value, ch_idx + 1))
            elif ch in curr:
                trees.append((curr[ch], ch_idx + 1))

        return False


        
