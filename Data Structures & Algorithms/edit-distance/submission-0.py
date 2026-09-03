class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        OPT = [[float('inf') for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]

        for i in range(len(word1), -1, -1):
            for j in range(len(word2), -1, -1):
                if i == len(word1):
                    OPT[i][j] = len(word2)-j
                elif j == len(word2):
                    OPT[i][j] = len(word1)-i
                elif (word1[i] != word2[j]):
                    OPT[i][j] = 1 + min(OPT[i+1][j], OPT[i][j+1], OPT[i+1][j+1])
                else:
                    OPT[i][j] = OPT[i+1][j+1]
        return OPT[0][0]