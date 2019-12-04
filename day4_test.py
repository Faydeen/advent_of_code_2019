import unittest
import day4 as puzzle
from aoc import read_file, timer

class TestBasic(unittest.TestCase):
    def test_pass(self):
        minVal, maxVal = puzzle.parse(read_file("04", "1"))
        result = puzzle.solve(minVal, maxVal)
        print(f"Solution: {result}")
    def testIsValidPassword(self):
        data = [1,0,0,0, 99]
        answer = puzzle.intComputer(data)
        self.assertEqual([2,0,0,0,99], answer)
    def testIsCodeValid(self):
        data = 111111
        answer = puzzle.isCodeValid(data)
        self.assertEqual(answer,True)
    def testIsCodeValid(self):
        data = 136779
        answer = puzzle.isCodeValid(data)
        self.assertEqual(answer, True)
    def testIsCodeValid(self):
        data = 136777
        answer = puzzle.isCodeValid(data)
        self.assertEqual(answer, False)
    def testIsCodeValid(self):
        data = 137777
        answer = puzzle.isCodeValid(data)
        self.assertEqual(answer, False)
    def testIsCodeValid(self):
        data = 137788
        answer = puzzle.isCodeValid(data)
        self.assertEqual(answer, True)
    def testIsCodeValid(self):
        data = 111144
        answer = puzzle.isCodeValid(data)
        self.assertEqual(answer, True)
if __name__ == '__main__':
    unittest.main()