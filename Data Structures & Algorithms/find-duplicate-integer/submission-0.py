class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0,0

        while True:
            slow = nums[slow]
            # fast only ever has one step over slow,
            # so it never skips over slow
            fast = nums[nums[fast]]

            # a = steps out of the cycle, b = steps in cycle
            # at this point, fast = 2(a + b)
            # slow = (a + b)
            # therefore fast - slow = a + b
            if slow == fast:
                break
        # if they met, that means there is m amount of full cycle loops between slow and fast
        # a + b = mc
        # a = mc - b => the # of steps to the entrance = 
        # the # of steps to complete the cycle at the entrance
        begin = 0
        while begin != slow: # will meet at the entrance
            slow = nums[slow]
            begin = nums[begin]

        return begin
            