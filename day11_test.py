import unittest
import day11 as puzzle
from aoc import read_file

import sys


class TestBasic(unittest.TestCase):
    def test_pass(self):
        data = puzzle.parse(read_file("11", "1"))
        result = puzzle.solve(data)
        print(f"Solution: {len(result.keys())}")
        self.assertEqual(True, True)

    def test_pass2(self):
        data = puzzle.parse(read_file("11", "1"))
        result = puzzle.solve2(data)
        for y in range(len(result)):
            for x in range(len(result[y])):
                if result[y][x] == 1:
                    sys.stdout.write("#")
                else:
                    sys.stdout.write(" ")
                sys.stdout.write("\n")
        self.assertEqual(True, True)


class TestUnitaire(unittest.TestCase):
    def testAdd(self):
        data = [1, 0, 0, 0, 99]
        answer = puzzle.solve(data)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
