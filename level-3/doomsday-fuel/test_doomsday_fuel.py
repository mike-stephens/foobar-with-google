import solution_doomsday_fuel
import unittest


class TestDoomsdayFuel(unittest.TestCase):

    def test_1(self):
        solution_input = [
            [0, 1, 0, 0, 0],
            [0, 0, 0, 3, 4],
            [0, 1, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        expected = [1, 1]
        result = solution_doomsday_fuel.solution(solution_input)
        self.assertEqual(result, expected)

    def test_2(self):
        solution_input = [
            [0, 2, 1, 0, 0],
            [0, 0, 0, 3, 4],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        expected = [7, 6, 8, 21]
        result = solution_doomsday_fuel.solution(solution_input)
        self.assertEqual(result, expected)

    def test_3(self):
        solution_input = [
            [0, 1, 0, 0, 0, 1],
            [4, 0, 0, 3, 2, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        expected = [0, 3, 2, 9, 14]
        result = solution_doomsday_fuel.solution(solution_input)
        self.assertEqual(result, expected)
