import solution_power_hungry
import unittest


class TestPowerHungry(unittest.TestCase):

    def test_1(self):
        solution_input = [2, 0, 2, 2, 0]
        expected = "8"
        result = solution_power_hungry.solution(solution_input)
        self.assertEqual(result, expected)

    def test_2(self):
        solution_input = [-2, -3, 4, -5]
        expected = "60"
        result = solution_power_hungry.solution(solution_input)
        self.assertEqual(result, expected)

    def test_3(self):
        solution_input = [0]
        expected = "0"
        result = solution_power_hungry.solution(solution_input)
        self.assertEqual(result, expected)

    def test_4(self):
        solution_input = [0, 0, 0]
        expected = "0"
        result = solution_power_hungry.solution(solution_input)
        self.assertEqual(result, expected)

    def test_5(self):
        solution_input = [-2]
        expected = "-2"
        result = solution_power_hungry.solution(solution_input)
        self.assertEqual(result, expected)

    def test_6(self):
        solution_input = [-2, 0]
        expected = "0"
        result = solution_power_hungry.solution(solution_input)
        self.assertEqual(result, expected)

    def test_7(self):
        solution_input = [0, 1, 0]
        expected = "1"
        result = solution_power_hungry.solution(solution_input)
        self.assertEqual(result, expected)

    def test_8(self):
        solution_input = [1]
        expected = "1"
        result = solution_power_hungry.solution(solution_input)
        self.assertEqual(result, expected)
