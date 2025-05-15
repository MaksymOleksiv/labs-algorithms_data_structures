import unittest
from ..src.main import amount_of_wire
from ..src.file_read import read_file

class TestMaxWireLength(unittest.TestCase):
    def test_case_1(self):
        w, h = read_file('case1.txt')
        self.assertAlmostEqual(amount_of_wire(w, h), 5.66)

    def test_case_2(self):
        w, h = read_file('case2.txt')
        self.assertAlmostEqual(amount_of_wire(w, h), 300.00)

    def test_case_3(self):
        w, h = read_file('case3.txt')
        self.assertAlmostEqual(amount_of_wire(w, h), 396.32)

    def test_case_4(self):
        w, h = read_file('case4.txt')
        self.assertAlmostEqual(
            amount_of_wire(w, h),
            2738.18, places=2)


if __name__ == '__main__':
    unittest.main()
