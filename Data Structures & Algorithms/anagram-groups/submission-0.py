class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_key(word):
            key = [0 for _ in range(26)]
            for ch in word:
                idx = ord(ch) - 97
                key[idx] += 1
            return tuple(key)

        anagrams = dict()

        for word in strs:
            key = get_key(word)
            if key not in anagrams:
                anagrams[key] = [word]
            else:
                anagrams[key].append(word)
        return list(anagrams.values())