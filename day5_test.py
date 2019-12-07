import unittest
import day5 as puzzle
import intcodeComputer
from aoc import read_file


class TestBasic(unittest.TestCase):
    def test_pass1(self):
        data = puzzle.parse(read_file("05", "1"))
        result = puzzle.solve(data, 1)
        print(result)

    def test_pass2(self):
        data = puzzle.parse(read_file("05", "2"))
        result = puzzle.solve(data, 5)
        print(result)

    def test_pass3(self):
        data = puzzle.parse(read_file("05", "3"))
        result = puzzle.solve(data, 1)
        print(result)

    def testGetActionCode(self):
        answer = intcodeComputer.getAction([1101], 0)
        self.assertEqual(1, answer)

    def testGetActionCode2(self):
        answer = intcodeComputer.getAction([1003], 0)
        self.assertEqual(3, answer)

    def testGetActionCode3(self):
        answer = intcodeComputer.getAction([4], 0)
        self.assertEqual(4, answer)

    def testGetActionCode4(self):
        answer = intcodeComputer.getAction([4], 0)
        self.assertEqual(4, answer)

    def testGetParam1(self):
        answer = intcodeComputer.getParam([1001, 1, 2, 3, 99], 0, 1)
        self.assertEqual(1, answer)

    def testGetParam2(self):
        answer = intcodeComputer.getParam([1001, 1, 3, 5, 99], 0, 2)
        self.assertEqual(3, answer)

    def testGetParam3(self):
        answer = intcodeComputer.getParam([105, 1, 3, 99], 0, 2)
        self.assertEqual(99, answer)

    def testGetParam4(self):
        answer = intcodeComputer.getParam([105, 1, 3, 2, 99], 0, 3)
        self.assertEqual(3, answer)

    def testSolve(self):
        data = [3, 0, 4, 0, 99]
        answer = puzzle.solve(data, 1)
        self.assertEqual(1, answer[0])

    def testSolve2(self):
        data = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
        answer = puzzle.solve(data, 1)
        self.assertEqual(999, answer[0])
        # Should print 1 if input = 8

    def testSolve2(self):
        data = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
        answer = puzzle.solve(data, 8)
        self.assertEqual(1000, answer[0])

    def testSolve3(self):
        data = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
                1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
                999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
        answer = puzzle.solve(data, 9)
        self.assertEqual(1001, answer[0])


if __name__ == '__main__':
    unittest.main()
