import unittest
import day15 as puzzle
from aoc import read_file


class TestBasic(unittest.TestCase):
    def test_pass(self):
        data = puzzle.parse(read_file("15", "1"))
        result = puzzle.solve(data)
        print(f"Solution: {result}")
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
