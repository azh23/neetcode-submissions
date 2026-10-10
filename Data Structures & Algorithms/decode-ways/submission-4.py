class Solution:
    def numDecodings(self, s: str) -> int:
        def valid_num(ten, one):
            if ten not in ["1", "2"]:
                return False
            if ten == "1":
                return True
            else:
                return one in "0123456"

        ways = [0] * len(s)
        if s[0] == "0":
            return 0
        ways[0] = 1
        if len(s) == 1:
            return 1
        if valid_num(s[0], s[1]):
            ways[1] = 2 if s[1] != "0" else 1
        elif s[1] == "0":
            return 0
        else:
            ways[1] = 1

        # absolute bullshit is above
        for i in range(2, len(s)):
            if s[i] == "0" and s[i - 1] not in ("1","2"):
                return 0
            if valid_num(s[i - 1], s[i]):
                if s[i] == "0":
                    ways[i] = ways[i - 2]
                else:
                    ways[i] = ways[i - 1] + ways[i - 2]
            else:
                ways[i] = ways[i - 1]
        print(ways)
        return ways[-1]



