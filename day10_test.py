import unittest
import day10 as puzzle
from aoc import read_file


class TestBasic(unittest.TestCase):
    def test_pass(self):
        data = puzzle.parse(read_file("10", "1"))
        location, numberOfAsteroidSeen = puzzle.solve(data)
        print(f"Solution: {location}, {numberOfAsteroidSeen}")
        self.assertEqual(location, (29, 28))
        self.assertEqual(numberOfAsteroidSeen, 256)

    def test_pass2(self):
        data = puzzle.parse(read_file("10", "1"))
        result = puzzle.solve_2(data, (29, 28))
        print(f"Solution: {result}")
        self.assertEqual(True, True)


class TestUnitaire(unittest.TestCase):
    def test_solve_1(self):
        data = puzzle.parse(["......#.#.", "#..#.#....", "..#######.", ".#.#.###..", ".#..#.....",
                             "..#....#.#", "#..#....#.", ".##.#..###", "##...#..#.", ".#....####"])
        location, numberOfAsteroidSeen = puzzle.solve(data)
        self.assertEqual(location, (5, 8))
        self.assertEqual(numberOfAsteroidSeen, 33)

    def test_solve_1_other(self):
        data = puzzle.parse('''#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.'''.split("\n"))
        location, numberOfAsteroidSeen = puzzle.solve(data)
        self.assertEqual(location, (1, 2))
        self.assertEqual(numberOfAsteroidSeen, 35)

    def test_solve_2(self):
        data = puzzle.parse('''.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##'''.split("\n"))
        result = puzzle.solve_2(data, (11, 13))
        self.assertEqual(result[1], (8, 2))


if __name__ == '__main__':
    unittest.main()
