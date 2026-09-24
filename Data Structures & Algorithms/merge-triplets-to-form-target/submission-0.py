class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        hasA = False
        hasB = False
        hasC = False

        tA, tB, tC = target

        for triplet in triplets:
            a, b, c = triplet
            if a == tA and b <= tB and c <= tC:
                hasA = True
            if b == tB and a <= tA and c <= tC:
                hasB = True
            if c == tC and a <= tA and b <= tB:
                hasC = True
        return hasA and hasB and hasC