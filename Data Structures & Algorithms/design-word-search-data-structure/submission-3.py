from collections import deque
class WordDictionary:

    def __init__(self):
        self.root = dict()

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr:
                curr[ch] = dict()
            curr = curr[ch]
        curr["$"] = dict()

    def search(self, word: str) -> bool:
        backlog = deque([self.root])

        for ch in word:
            backlen = len(backlog)
            for _ in range(backlen):
                curr = backlog.popleft()
                if ch == ".":
                    backlog.extend(curr.values())
                elif ch in curr:
                    backlog.append(curr[ch])
            if len(backlog) == 0:
                return False
        return any("$" in node for node in backlog)
