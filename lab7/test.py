import unittest
from main import search_dfa

class TestDFASearch(unittest.TestCase):
    def test_single_occurrence(self):
        self.assertEqual(search_dfa("abcde", "bcd"), [1])

    def test_multiple_occurrences(self):
        self.assertEqual(search_dfa("hellohello", "hello"), [0, 5])

    def test_overlapping_occurrences(self):
        self.assertEqual(search_dfa("aaaaa", "aaa"), [0, 1, 2])

    def test_no_occurrence(self):
        self.assertEqual(search_dfa("abcdef", "xyz"), [])

    def test_needle_equals_haystack(self):
        self.assertEqual(search_dfa("hello", "hello"), [0])

    def test_empty_needle(self):
        self.assertEqual(search_dfa("abc", ""), [])

    def test_empty_haystack(self):
        self.assertEqual(search_dfa("", "abc"), [])

    def test_both_empty(self):
        self.assertEqual(search_dfa("", ""), [])

if __name__ == '__main__':
    unittest.main()
