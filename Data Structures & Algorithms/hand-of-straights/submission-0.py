from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = Counter(hand)

        while len(counts) >= groupSize:
            card = next(iter(counts))
            if card - 1 in counts:
                card = card - 1

            for _ in range(groupSize):
                if card in counts:
                    counts[card] -= 1
                    if counts[card] == 0:
                        counts.pop(card, None)
                else:
                    return False
                
                card += 1

        return len(counts) == 0

                    