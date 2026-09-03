class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        => init all False except OPT[0] == True
        OPT[i] = if s[:i] can be broken into words
        for word in wordDict:
            OPT[i + len(word)] = OPT[i]
        """
        OPT = [False for _ in range(len(s) + 1)]
        OPT[0] = True

        for i in range(len(s) + 1):
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    OPT[i + len(word)] = OPT[i] or OPT[i + len(word)]

        return OPT[len(s)]
