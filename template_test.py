import unittest
import day10 as puzzle
from aoc import read_file


class TestBasic(unittest.TestCase):
    def test_pass(self):
        data = puzzle.parse(read_file("02", "1"))
        result = puzzle.solve(data)
        print(f"Solution: {result}")
        self.assertEqual(True, True)


class TestUnitaire(unittest.TestCase):
    def testAdd(self):
        data = [1, 0, 0, 0, 99]
        answer = puzzle.solve(data)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
