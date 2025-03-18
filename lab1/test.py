import unittest
from main import zigzag_matrix


class TestZigzagTraversal(unittest.TestCase):
    def test_square_matrix(self):
        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        expected = [1, 2, 6, 11, 7, 3, 4, 8, 12, 16, 21, 17, 13, 9, 5, 10, 14, 18, 22, 23, 19, 15, 20, 24, 25]
        self.assertEqual(zigzag_matrix(matrix), expected)

    def test_rectangle_matrix(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]
        expected = [1, 2, 5, 6, 3, 4, 7, 8]
        self.assertEqual(zigzag_matrix(matrix), expected)

    def test_single_column(self):
        matrix = [
            [1], [2], [3], [4], [5], [6]
        ]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(zigzag_matrix(matrix), expected)

    def test_single_row(self):
        matrix = [[1, 2, 3, 4, 5]]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(zigzag_matrix(matrix), expected)

    def test_single_element(self):
        matrix = [[1]]
        expected = [1]
        self.assertEqual(zigzag_matrix(matrix), expected)


if __name__ == "__main__":
    unittest.main()
