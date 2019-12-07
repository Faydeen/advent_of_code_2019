import unittest
import day4 as puzzle
from aoc import read_file


class TestBasic(unittest.TestCase):
    def test_pass(self):
        minVal, maxVal = puzzle.parse(read_file("04", "1"))
        result = puzzle.solve(minVal, maxVal)
        self.assertEqual(result, 1264)

    def testcheckForDoublon(self):
        data = 111111
        answer = puzzle.checkForDoublon(data)
        self.assertEqual(answer, False)

    def testcheckForDoublon2(self):
        data = 136779
        answer = puzzle.checkForDoublon(data)
        self.assertEqual(answer, True)

    def testcheckForDoublon3(self):
        data = 136777
        answer = puzzle.checkForDoublon(data)
        self.assertEqual(answer, False)

    def testcheckForDoublon4(self):
        data = 137777
        answer = puzzle.checkForDoublon(data)
        self.assertEqual(answer, False)

    def testcheckForDoublon5(self):
        data = 137788
        answer = puzzle.checkForDoublon(data)
        self.assertEqual(answer, True)

    def testcheckForDoublon6(self):
        data = 111144
        answer = puzzle.checkForDoublon(data)
        self.assertEqual(answer, True)


if __name__ == '__main__':
    unittest.main()
