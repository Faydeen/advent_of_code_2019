import unittest
import day13 as puzzle
from aoc import read_file


class TestBasic(unittest.TestCase):
    # def test_pass(self):
    #     data = puzzle.parse(read_file("13", "1"))
    #     result = puzzle.solve(data)
    #     print(f"Solution: {result}")
    #     self.assertEqual(result, 205)

    def test_pass2(self):
        data = puzzle.parse(read_file("13", "1"))
        result = puzzle.solve2(data)
        print(f"Solution: {result}")
        self.assertEqual(result, 205)


if __name__ == '__main__':
    unittest.main()
