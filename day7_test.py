import unittest
import day7 as puzzle
from aoc import read_file

import itertools


class TestBasic(unittest.TestCase):
    # def test_pass(self):
    #     data = puzzle.parse(read_file("07", "1"))
    #     result = puzzle.solve(data)
    #     print(f"Solution: {result}")

    # def testAdd(self):
    #     data = [0, 1, 2, 3, 4]
    #     answer = itertools.permutations(data, 5)
    #     for order in itertools.permutations([0, 1, 2, 3, 4], 5):
    #         print(order)
    #     self.assertEqual(True, True)

    def testAllAccu(self):
        data = puzzle.parse(read_file("07", "1"))
        result = puzzle.allAccu(data, (4, 3, 2, 1, 0))
        print(result)


if __name__ == '__main__':
    unittest.main()
