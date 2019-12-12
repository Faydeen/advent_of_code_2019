import unittest
import day12 as puzzle
from aoc import read_file


class TestBasic(unittest.TestCase):
    def test_pass(self):
        data = puzzle.parse(read_file("12", "1"))
        result = puzzle.solve(data, 1000)
        self.assertEqual(result, 9876)

    def test_pass2(self):
        data = puzzle.parse(read_file("12", "1"))
        result = puzzle.solve2(data)
        self.assertEqual(result, 307043147758488)


class TestUnitaire(unittest.TestCase):
    def testExample(self):
        data = puzzle.parse(["<x=-1, y=0, z=2>", "<x=2, y=-10, z=-7>",
                             "<x=4, y=-8, z=8>", "<x=3, y=5, z=-1>"])
        answer = puzzle.solve(data, 10)
        self.assertEqual(answer, 179)

    def testExample2(self):
        data = puzzle.parse(["<x=-1, y=0, z=2>", "<x=2, y=-10, z=-7>",
                             "<x=4, y=-8, z=8>", "<x=3, y=5, z=-1>"])
        answer = puzzle.solve2(data)
        self.assertEqual(answer, 2772)

    def testExample3(self):
        data = puzzle.parse(
            ["<x=-8, y=-10, z=0>", "<x=5, y=5, z=10>", "<x=2, y=-7, z=3>", "<x=9, y=-8, z=-3>"])
        answer = puzzle.solve2(data)
        self.assertEqual(answer, 4686774924)


if __name__ == '__main__':
    unittest.main()
