from stack import Stack
from copy import deepcopy


def fillField(field, point, color):
    target_color = field[point[0]][point[1]]
    if target_color == color:
        return field

    stack = Stack()
    stack.push(point)

    while not stack.isEmpty():
        i, j = stack.pop()

        if 0 <= i < len(field) and 0 <= j < len(field[0]) and field[i][j] == target_color:
            field[i][j] = color

            stack.push((i + 1, j))
            stack.push((i - 1, j))
            stack.push((i, j + 1))
            stack.push((i, j - 1))

    return field
