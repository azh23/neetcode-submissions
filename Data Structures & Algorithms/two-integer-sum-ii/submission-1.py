class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        begin = 0
        end = len(numbers) - 1

        while begin < end:
            combo = numbers[begin] + numbers[end]
            if combo == target:
                return [begin+1, end+1]
            elif combo < target:
                begin += 1
            else:
                end -= 1
        return []