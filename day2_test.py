import unittest
import day2
from aoc import read_file


class TestResultat(unittest.TestCase):
    def test_pass(self):
        data = day2.parse(read_file("02", "1"))
        day2.solve(data, 12, 2)
        print(f"Solution: {data[0]}")
        self.assertEqual(data[0], 5534943)

    def test_pass2(self):
        data = day2.parse(read_file("02", "2"))
        resultat = 0
        for noun in range(0, len(data)):
            for verb in range(0, len(data)):
                result = day2.solve(data, noun, verb)
                if result[0] == 19690720:
                    resultat = 100*noun + verb
                    break
                data = day2.parse(read_file("02", "2"))
            if resultat != 0:
                break
        self.assertEqual(result, 7603)


class TestUnitaire(unittest.TestCase):
    def testAdd(self):
        data = [1, 0, 0, 0, 99]
        day2.solve(data)
        self.assertEqual([2, 0, 0, 0, 99], data)

    def testMult(self):
        data = [2, 0, 0, 0, 99]
        day2.solve(data)
        self.assertEqual([4, 0, 0, 0, 99], data)

    def testComplet(self):
        data = [2, 0, 0, 0, 1, 0, 4, 1, 99]
        day2.solve(data)
        self.assertEqual([4, 5, 0, 0, 1, 0, 4, 1, 99], data)


if __name__ == '__main__':
    unittest.main()
