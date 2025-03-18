import unittest
from main import max_hamster


class Test(unittest.TestCase):
    def test_1(self):
        hamster = [[1, 2], [2, 2], [3, 1]]
        self.assertEqual(max_hamster(7, 3, hamster), 2)

    def test_2(self):
        hamster = [[5, 0], [2, 2], [1, 4], [5, 1]]
        self.assertEqual(max_hamster(19, 4, hamster), 3)

    def test_3(self):
        hamster = [[1, 50000], [1, 60000]]
        self.assertEqual(max_hamster(2, 2, hamster), 1)


print(max_hamster(7, 3, [[1, 2], [2, 2], [3, 1]]))
print(max_hamster(19, 4, [[5, 0], [2, 2], [1, 4], [5, 1]]))
print(max_hamster(2, 2, [[1, 50000], [1, 60000]]))
print(max_hamster(10, 3, [[2, 3], [3, 1], [1, 5]]))
