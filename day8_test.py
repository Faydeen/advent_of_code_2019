import unittest
import day8 as puzzle
from aoc import read_file
import matplotlib.pyplot as plt


class TestBasic(unittest.TestCase):
    def test_pass(self):
        data = puzzle.parse(read_file("08", "1"), 25, 6)
        result = puzzle.solve(data)
        print(f"Solution: {result}")
        self.assertEqual(result[1], 2500)

    def test_pass(self):
        data = puzzle.parse(read_file("08", "1"), 25, 6)
        result = puzzle.solve2(data)
        plt.imshow(result, 'gray')
        # plt.show()
        #print(f"Solution: {result}")


class TestUnitaire(unittest.TestCase):
    def test_parse(self):
        data = ["123456789012"]
        answer = puzzle.parse(data, 3, 2)
        self.assertEqual(len(answer), 2)

    def test_countZeroOnLayer(self):
        data = ["000000000000"]
        result = puzzle.countZeroOnLayer([[0, 1, 2, 3], [0, 0, 2, 5]])
        self.assertEqual((3, 2), result)

    def test_countZeroOnLayer2(self):
        layer = [
            [2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
                2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2],
            [2, 2, 0, 2, 2, 2, 0, 2, 0, 2, 2, 2, 2,
                2, 2, 2, 2, 2, 2, 0, 2, 2, 0, 2, 2],
            [2, 0, 2, 2, 0, 2, 2, 0, 1, 2, 1, 2, 2,
                2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2],
            [2, 0, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2,
                2, 2, 1, 2, 2, 2, 0, 1, 2, 2, 2, 0],
            [2, 2, 2, 2, 0, 2, 0, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2]]
        result = puzzle.countZeroOnLayer(layer)
        self.assertEqual((16, 714), result)


if __name__ == '__main__':
    unittest.main()
