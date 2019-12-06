import unittest
import day6 as puzzle
from aoc import read_file


class TestBasic(unittest.TestCase):
    # def test_pass(self):
    #     data = puzzle.parse(read_file("06", "1"))
    #     result = puzzle.solve(data)
    #     print(f"Solution: {result}")
    #     self.assertEqual(True, True)
    def test_pass2(self):
        data = puzzle.parse(read_file("06", "1"))
        result = puzzle.solve_2(data, "YOU", "SAN")
        print(f"Solution: {result}")
        self.assertEqual(True, True)
    # def testSolveOneInput(self):
    #     data = ["A)B"]
    #     for line in data:
    #         print("####")
    #         print(line)
    #     input = puzzle.parse(data)
    #     print(input)
    #     print(len(input.heads))
    #     print(input.heads[0])
    #     print(input.heads[0].children)
    #     answer = puzzle.solve(input)
    #     self.assertEqual(1, answer)

    # def testParseOneInput(self):
    #     data = ["A)B"]
    #     linkedList = puzzle.parse(data)
    #     self.assertEqual("A", linkedList.heads[0].data)
    #     self.assertEqual("B", linkedList.heads[0].children[0].data)

    # def testParsetwoInputAtEnd(self):
    #     data = ["A)B", "B)C"]
    #     linkedList = puzzle.parse(data)
    #     self.assertEqual("A", linkedList.heads[0].data)
    #     self.assertEqual("B", linkedList.heads[0].children[0].data)
    #     self.assertEqual(1, len(linkedList.heads[0].children[0].children))
    #     self.assertEqual(
    #         "C", linkedList.heads[0].children[0].children[0].data)

    # def testParsetwoInputAtBeginning(self):
    #     data = ["A)B", "C)A"]
    #     linkedList = puzzle.parse(data)
    #     self.assertEqual(1, len(linkedList.heads))
    #     self.assertEqual("C", linkedList.heads[0].data)
    #     self.assertEqual("A", linkedList.heads[0].children[0].data)
    #     self.assertEqual(
    #         "B", linkedList.heads[0].children[0].children[0].data)

    # def testParsetwoInputTwoHead(self):
    #     data = ["A)B", "C)D"]
    #     linkedList = puzzle.parse(data)

    #     self.assertEqual(2, len(linkedList.heads))
    #     self.assertEqual("A", linkedList.heads[0].data)
    #     self.assertEqual("B", linkedList.heads[0].children[0].data)
    #     self.assertEqual("C", linkedList.heads[1].data)
    #     self.assertEqual("D", linkedList.heads[1].children[0].data)


if __name__ == '__main__':
    unittest.main()
