"""
unittest for binary search
"""
import random
import unittest

from py23.algorithms.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):

    def setUp(self):
        self.data = list(range(1000))

    def test_binary_search_find(self):
        for _ in range(100):
            target = random.randint(0,999)
            self.assertEqual(
                binary_search(self.data, len(self.data), target),
                self.data.index(target)
            )
    
    def test_binary_search_not_find(self):
        self.assertEqual(
            binary_search(self.data, len(self.data), 20000),
            -1
        )
        self.assertEqual(
            binary_search(self.data, len(self.data), -1),
            -1
        )

if __name__ == '__main__':
    unittest.main()
