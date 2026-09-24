class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parens = []
        stack = []

        def backtrack(opn, clo):
            if opn == n and clo == n:
                parens.append("".join(stack))
                return
            
            if opn < n:
                stack.append("(")
                backtrack(opn + 1, clo)
                stack.pop()
            if clo < opn:
                stack.append(")")
                backtrack(opn, clo + 1)
                stack.pop()

        backtrack(0,0)
        return parens