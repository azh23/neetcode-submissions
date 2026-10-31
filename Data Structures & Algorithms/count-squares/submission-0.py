from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.pts = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.pts[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        x1, y1 = point
        column = self.pts.get(x1, {})
        for y2, cnt in column.items():
            side = y2 - y1
            if side == 0:
                continue
            x3, x4 = x1 + side, x1 - side
            for x in (x3, x4):
                counts = self.pts.get(x, {})
                res += cnt * counts.get(y1, 0) * counts.get(y2, 0)
        return res
        
