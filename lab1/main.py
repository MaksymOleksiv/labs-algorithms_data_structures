def zigzag_matrix(matrix):
    if not matrix or not matrix[0]:
        return []

    result = []
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, 0
    right_up = True

    while len(result) < rows * cols:
        result.append(matrix[row][col])

        if right_up:
            if col == cols - 1:
                row += 1
                right_up = False
            elif row == 0:
                col += 1
                right_up = False
            else:
                row -= 1
                col += 1
        else:
            if row == rows - 1:
                col += 1
                right_up = True
            elif col == 0:
                row += 1
                right_up = True
            else:
                row += 1
                col -= 1
    return result
