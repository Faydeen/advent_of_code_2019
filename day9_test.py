import unittest
import day9 as puzzle
from aoc import read_file


class TestBasic(unittest.TestCase):
    def test_pass(self):
        data = puzzle.parse(read_file("09", "1"))
        result = puzzle.solve(data, [1])
        print(f"Solution: {result}")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], 2351176124)

    def test_pass2(self):
        data = puzzle.parse(read_file("09", "1"))
        result = puzzle.solve(data, [2])
        print(f"Solution: {result}")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], 73110)


class TestUnitaire(unittest.TestCase):
    def test_quine_computer(self):
        data = [109, 1, 204, -1, 1001, 100, 1, 100,
                1008, 100, 16, 101, 1006, 101, 0, 99]

        answer = puzzle.solve(data)
        self.assertEqual([109, 1, 204, -1, 1001, 100, 1, 100,
                          1008, 100, 16, 101, 1006, 101, 0, 99], answer)

    def test_16_digit_number(self):
        data = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]

        answer = puzzle.solve(data)
        self.assertEqual(len(str(answer[0])), 16)

    def test_print_middle_number(self):
        data = [104, 1125899906842624, 99]

        answer = puzzle.solve(data)
        self.assertEqual(answer[0], 1125899906842624)


if __name__ == '__main__':
    unittest.main()
