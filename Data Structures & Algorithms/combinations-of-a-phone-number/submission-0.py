class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        combinations = []
        translate = {
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p","q","r","s"],
            "8" : ["t","u","v"],
            "9" : ["w","x","y","z"],
        }

        def backtrack(idx, output):
            if len(output) == len(digits):
                combinations.append("".join(output))
                return

            for char in translate[digits[idx]]:
                output.append(char)
                backtrack(idx + 1, output)
                output.pop()
        backtrack(0, [])
        return combinations