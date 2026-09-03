from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        letters = list('abcdefghijklmnopqrstuvwxyz')

        q = deque()
        q.append((beginWord,0))
        processed = set()
        processed.add(beginWord)
        while q:
            curr, steps = q.popleft()
            if curr == endWord:
                return steps + 1
            for i, ch in enumerate(curr):
                for letter in letters:
                    new_curr = curr[:i] + letter + curr[i + 1:]
                    if new_curr in words and new_curr not in processed:
                        q.append((new_curr, steps + 1))
                        processed.add(new_curr)
        return 0

