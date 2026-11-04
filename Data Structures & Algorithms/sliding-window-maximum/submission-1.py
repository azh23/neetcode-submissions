from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        
        for idx in range(k):
            if q and nums[idx] > nums[q[0]]:
                q = deque()
            if q and nums[idx] > nums[q[-1]]:
                while nums[idx] > nums[q[-1]]:
                    q.pop()
            q.append(idx)

        res = [0] * (len(nums) - k + 1)
        res[0] = nums[q[0]]

        for rm in range(len(nums) - k):
            add = rm + k
            if q[0] == rm:
                q.popleft()

            if q and nums[add] > nums[q[0]]:
                q = deque()
            if q and nums[add] > nums[q[-1]]:
                while nums[add] > nums[q[-1]]:
                    q.pop()
            q.append(add)
            """
            pr = str(rm) + ":"
            for item in q:
                pr += str(nums[item]) + ","
            print(pr)
            """
            res[rm + 1] = nums[q[0]]
        return res