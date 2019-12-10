import unittest
import day10 as puzzle
from aoc import read_file


class TestBasic(unittest.TestCase):
    def test_pass(self):
        data = puzzle.parse(read_file("10", "1"))
        location, numberOfAsteroidSeen = puzzle.solve(data, 12, 2)
        print(f"Solution: {location}, {numberOfAsteroidSeen}")
        self.assertEqual(True, True)


class TestUnitaire(unittest.TestCase):
    def test_solve_1(self):
        data = puzzle.parse('''......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####''')
        location, numberOfAsteroidSeen = puzzle.solve(data)
        self.assertEqual(location, (5, 8))
        self.assertEqual(numberOfAsteroidSeen, 33)


def test_solve_2(self):
    data = puzzle.parse('''#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.''')
    location, numberOfAsteroidSeen = puzzle.solve(data)
    self.assertEqual(location, (1, 2))
    self.assertEqual(numberOfAsteroidSeen, 35)


if __name__ == '__main__':
    unittest.main()
