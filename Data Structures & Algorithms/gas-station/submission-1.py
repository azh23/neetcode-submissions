class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        result = 0
        if sum(gas) < sum(cost):
            return -1 

        for idx in range(len(gas)):
            total += gas[idx] - cost[idx]
            if total < 0:
                result = idx + 1
                total = 0        
        return result
