class Solution:
    def decodeString(self, s: str) -> str:
        encode = []
        res = ""

        i = 0

        while i < len(s):
            if s[i].isdigit():
                k = 0
                while s[i].isdigit():
                    k = k * 10 + int(s[i])
                    i += 1 # i ends at [
                encode.append([k, ""])
            elif s[i] == "]":
                # terminate a "string"
                k, part = encode.pop()
                inside = k * part
                if encode:
                    encode[-1][1] += inside
                else:
                    res += inside
            else:
                # regular char
                if encode:
                    encode[-1][1] += s[i]
                else:
                    res += s[i]
            i += 1
        return res

