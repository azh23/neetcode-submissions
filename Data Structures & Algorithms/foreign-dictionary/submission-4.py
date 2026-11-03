from collections import defaultdict, deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjacency = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adjacency}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for ch1, ch2 in zip(w1, w2):
                if ch1 != ch2:
                    if ch2 not in adjacency[ch1]:
                        adjacency[ch1].add(ch2)
                        indegree[ch2] += 1
                    break
        
        q = deque([c for c in indegree if indegree[c] == 0])
        res = []
        while q:
            ch = q.popleft()
            res.append(ch)

            for nei in adjacency[ch]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        if len(res) != len(indegree):
            return ""
        return "".join(res)
