class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += "#"
            res += s
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        lst = []
        idx = 0

        while idx < len(s):
            j = idx
            while s[j] != "#":
                j += 1
            s_len = int(s[idx:j])
            idx = j + 1
            j = idx + s_len
            lst.append(s[idx:j])
            idx = j
        return lst
