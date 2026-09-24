class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        width = len(matrix[0])
        height = len(matrix) - 1
        x, y = 0, 0
        xrev, yrev = 1, 1
        spiral = []
        while width:
            print("w, h:",width,height)
            for w in range(width):
                print(y,x)
                spiral.append(matrix[y][x])
                x += 1 * xrev
            x -= 1 * xrev
            for h in range(height):
                y += 1 * yrev
                print(y,x)
                spiral.append(matrix[y][x])
            xrev *= -1
            yrev *= -1
            x += 1 * xrev
            width -= 1
            if not height:
                break
            height -= 1
            print("w, h:",width,height)
        return spiral


