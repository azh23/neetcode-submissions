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

"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert list to set for O(1) lookups
        word_set = set(wordDict)
        
        # dp[i] means s[0:i] can be segmented into dictionary words
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Base case
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                # If prefix s[0:j] is valid AND substring s[j:i] is a valid word
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # Found a valid split for dp[i], move to next i
                    
        return dp[len(s)]
"""