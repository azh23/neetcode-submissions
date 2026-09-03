class Solution:
    def isValid(self, s: str) -> bool:
        pairs = { ")" : "(", "}" : "{", "]" : "["}
        stack = []

        for ch in s:
            if ch not in pairs:
                stack.append(ch)
            else:
                if stack and stack[-1] == pairs[ch]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0