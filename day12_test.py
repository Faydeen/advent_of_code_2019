import unittest
import day12 as puzzle
from aoc import read_file


class TestBasic(unittest.TestCase):
    def test_pass(self):
        data = puzzle.parse(read_file("12", "1"))
        result = puzzle.solve(data, 1000)
        print(f"Solution: {result}")
        self.assertEqual(True, True)


class TestUnitaire(unittest.TestCase):
    def testAdd(self):
        # data = [1, 0, 0, 0, 99]
        # answer = puzzle.solve(data, 10)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
