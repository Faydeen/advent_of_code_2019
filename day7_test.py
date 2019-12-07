import unittest
import day7 as puzzle
from aoc import read_file

import itertools


class TestBasic(unittest.TestCase):
    def test_pass(self):
        data = puzzle.parse(read_file("07", "1"))
        result = puzzle.solve(data)
        self.assertEqual(result, 212460)

    def test_pass2(self):
        data = puzzle.parse(read_file("07", "1"))
        result = puzzle.solve2(data)
        self.assertEqual(result, 21844737)


if __name__ == '__main__':
    unittest.main()
