import unittest
import day14 as puzzle
from aoc import read_file


class TestBasic(unittest.TestCase):
    def test_pass(self):
        data = puzzle.parse(read_file("14", "1"))
        result = puzzle.solve(data)
        print(f"Solution: {result}")
        self.assertEqual(result, 628586)

    def test_pass2(self):
        data = puzzle.parse(read_file("14", "1"))
        result = puzzle.solve2(data)
        print(f"Solution: {result}")
        self.assertEqual(result, 3209254)


class TestUnitaire(unittest.TestCase):
    def test1(self):
        input = '''9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL'''.split('\n')
        data = puzzle.parse(input)
        answer = puzzle.solve(data)
        self.assertEqual(answer, 165)

    def test2(self):
        data = puzzle.parse('''157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT'''.split('\n'))
        answer = puzzle.solve(data)
        self.assertEqual(answer, 13312)


if __name__ == '__main__':
    unittest.main()
