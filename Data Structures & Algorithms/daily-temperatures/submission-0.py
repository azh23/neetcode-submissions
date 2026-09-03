class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        temps = [0 for _ in range(len(temperatures))]

        for idx, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                past = stack.pop()
                temps[past] = idx - past
            stack.append(idx)
        return temps