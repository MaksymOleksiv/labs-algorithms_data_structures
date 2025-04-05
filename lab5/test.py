import unittest
from main import fillField
import copy


class TestFillField(unittest.TestCase):
    def setUp(self):
        self.original_matrix = [
            ['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
            ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
            ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ]

    def test_fill_from_3_9(self):
        expected_result = [
            ['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'C', 'C', 'C'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'C', 'C', 'C'],
            ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'C'],
            ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'C', 'C', 'C'],
            ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'C', 'C', 'C'],
            ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'C'],
            ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'C', 'C', 'C'],
            ['W', 'B', 'B', 'C', 'B', 'B', 'B', 'B', 'C', 'C'],
            ['W', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'C'],
        ]
        matrix_copy = copy.deepcopy(self.original_matrix)
        result = fillField(matrix_copy, (3, 9), 'C')
        self.assertEqual(result, expected_result)

    def test_fill_from_0_0(self):
        expected_result = [
            ['Z', 'Z', 'Z', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['Z', 'Z', 'Z', 'Z', 'Z', 'Z', 'G', 'X', 'X', 'X'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
            ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
            ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
        ]
        matrix_copy = copy.deepcopy(self.original_matrix)
        result = fillField(matrix_copy, (0, 0), 'Z')
        self.assertEqual(result, expected_result)

    def test_no_change_when_same_color(self):
        matrix_copy = copy.deepcopy(self.original_matrix)
        result = fillField(matrix_copy, (0, 0), 'Y')
        self.assertEqual(result, self.original_matrix)


if __name__ == '__main__':
    unittest.main()
