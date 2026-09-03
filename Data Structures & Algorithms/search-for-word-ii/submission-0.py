class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = dict()

        for word in words:
            curr_trie = trie
            for ch in word:
                if ch not in curr_trie:
                    curr_trie[ch] = dict()
                curr_trie = curr_trie[ch]
            curr_trie["$"] = dict()
        present = set()

        def dfs(row, col, trie, word):
            nonlocal present
            if "$" in trie:
                present.add(word)
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return
            if board[row][col] in trie:
                saved = board[row][col]
                board[row][col] = "0"

                dfs(row + 1, col, trie[saved], word + saved)
                dfs(row, col + 1, trie[saved], word + saved)
                dfs(row - 1, col, trie[saved], word + saved)
                dfs(row, col - 1, trie[saved], word + saved)


                board[row][col] = saved
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r, c, trie, "")
        return list(present)
