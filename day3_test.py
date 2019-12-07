import unittest
import day3 as puzzle
from aoc import read_file


class TestBasic(unittest.TestCase):
    def test_pass(self):
        data = puzzle.parse(read_file("03", "2"))
        result = puzzle.solve(data)[1]
        print(f"Solution: {result}")
        self.assertEqual(result, 27890)

    def testRight(self):
        input = ["R10", "L10"]
        answer = puzzle.parse(input)
        self.assertEqual(([(0, 0), (10, 0)], [(0, 0), (-10, 0)]), answer)

    def testUp(self):
        input = ["U10", "D10"]
        answer = puzzle.parse(input)
        self.assertEqual(([(0, 0), (0, 10)], [(0, 0), (0, -10)]), answer)

    def testIntersectWhenNoIntPoint(self):
        segment1, segment2 = (((1, 10), (2, 10)), ((-1, -10), (-2, -10)))
        intersect, point = puzzle.intersectionPoint(segment1, segment2)
        self.assertEqual(intersect, False)
        self.assertEqual(point, (0, 0))

    def testIntersectWhenNoIntPoint(self):
        segment1, segment2 = (((1, 5), (10, 5)), ((7, 0), (7, 10)))
        intersect, point = puzzle.intersectionPoint(segment1, segment2)
        self.assertEqual(intersect, True)
        self.assertEqual(point, (7, 5))

    def testNbStepWhenAtEnd(self):
        coords = ((0, 0), (0, 10), (10, 10))
        targetPoint = (10, 10)
        answer = puzzle.nbStep(coords, targetPoint)
        self.assertEqual(answer, 20)

    def testNbStepWhenAtEnd(self):
        coords = ((0, 0), (0, -10), (-10, -10))
        targetPoint = (0, -10)
        answer = puzzle.nbStep(coords, targetPoint)
        self.assertEqual(answer, 10)

    def testNbStepWhenAtEnd(self):
        coords = ((0, 0), (0, 10), (10, 10))
        targetPoint = (5, 10)
        answer = puzzle.nbStep(coords, targetPoint)
        self.assertEqual(answer, 15)

    def testNbStepWhenAtEnd(self):
        coords = ((0, 0), (0, -10), (10, 10))
        targetPoint = (0, -5)
        answer = puzzle.nbStep(coords, targetPoint)
        self.assertEqual(answer, 5)


if __name__ == '__main__':
    unittest.main()
