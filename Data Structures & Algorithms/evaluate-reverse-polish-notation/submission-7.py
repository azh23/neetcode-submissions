class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        operands = set(['+', '-', '*', '/'])
        for token in tokens:
            if token in operands:
                num2 = nums.pop()
                num1 = nums.pop()
                #print(num1, token, num2)
                match token:
                    case '+':
                        res = num1 + num2
                    case '-':
                        res = num1 - num2
                    case '*':
                        res = num1 * num2
                    case _:
                        res = int(num1/num2)
                nums.append(res)
            else:
                nums.append(int(token))
        #print(nums)
        return nums[0]
