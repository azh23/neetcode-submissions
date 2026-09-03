class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        prefix = [0 for _ in range(len(height))]
        suffix = [0 for _ in range(len(height))]

        pfix = 0
        sfix = 0
        for i in range(len(height)):
            pfix = max(pfix, height[i])
            prefix[i] = pfix

            sfix = max(sfix, height[-(i+1)])
            suffix[-(i+1)] = sfix
        water = 0
        for i in range(len(height)):
            w = min(prefix[i], suffix[i]) - height[i]
            water += min(prefix[i], suffix[i]) - height[i]
        return water
            

