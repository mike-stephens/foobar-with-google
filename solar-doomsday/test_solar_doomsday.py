import solution_solar_doomsday
import unittest


class TestSolarDoomsday(unittest.TestCase):

    def test_1(self):
        solution_input = 15324
        expected = [15129, 169, 25, 1]
        result = solution_solar_doomsday.solution(solution_input)
        self.assertEqual(result, expected)

    def test_2(self):
        solution_input = 12
        expected = [9, 1, 1, 1]
        result = solution_solar_doomsday.solution(solution_input)
        self.assertEqual(result, expected)
