class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row = 0 in matrix[0]
        first_col = len([x for x in matrix if x[0] == 0]) > 0

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if first_row:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        if first_col:
            for r in range(len(matrix)):
                matrix[r][0] = 0