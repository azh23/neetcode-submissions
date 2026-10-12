class Solution:
    def partition(self, s: str) -> List[List[str]]:
        lst = []

        def is_palindrome(word):
            for i in range(len(word) // 2):
                if word[i] != word[len(word) - i - 1]:
                    return False
            return True

        def backtrack(idx, arr):
            if idx == len(s):
                lst.append(arr[:])
            
            substr = ""
            for i in range(idx, len(s)):
                substr += s[i]
                if is_palindrome(substr):
                    arr.append(substr)
                    backtrack(i + 1, arr)
                    arr.pop()
        backtrack(0, [])
        return lst