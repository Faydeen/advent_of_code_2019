import unittest
import day2 as puzzle
from aoc import read_file


class TestBasic(unittest.TestCase):
    def test_pass(self):
        data = puzzle.parse(read_file("02", "1"))
        result = puzzle.solve(data, 12, 2)
        print(f"Solution: {result}")

    def testAdd(self):
        data = [1, 0, 0, 0, 99]
        answer = puzzle.intComputer(data)
        self.assertEqual([2, 0, 0, 0, 99], answer)


if __name__ == '__main__':
    unittest.main()
