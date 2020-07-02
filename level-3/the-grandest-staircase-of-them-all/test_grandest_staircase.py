import solution_grandest_staircase
import unittest


class TestGrandestStaircase(unittest.TestCase):

    def test_1(self):
        solution_input = 3
        expected = 1
        result = solution_grandest_staircase.solution(solution_input)
        self.assertEqual(result, expected)

    def test_2(self):
        solution_input = 4
        expected = 1
        result = solution_grandest_staircase.solution(solution_input)
        self.assertEqual(result, expected)

    def test_3(self):
        solution_input = 5
        expected = 2
        result = solution_grandest_staircase.solution(solution_input)
        self.assertEqual(result, expected)

    def test_4(self):
        solution_input = 6
        expected = 3
        result = solution_grandest_staircase.solution(solution_input)
        self.assertEqual(result, expected)

    def test_5(self):
        solution_input = 7
        expected = 4
        result = solution_grandest_staircase.solution(solution_input)
        self.assertEqual(result, expected)

    def test_6(self):
        solution_input = 10
        expected = 9
        result = solution_grandest_staircase.solution(solution_input)
        self.assertEqual(result, expected)

    def test_7(self):
        solution_input = 25
        expected = 141
        result = solution_grandest_staircase.solution(solution_input)
        self.assertEqual(result, expected)

    def test_8(self):
        solution_input = 75
        expected = 48445
        result = solution_grandest_staircase.solution(solution_input)
        self.assertEqual(result, expected)

    def test_9(self):
        solution_input = 137
        expected = 7755775
        result = solution_grandest_staircase.solution(solution_input)
        self.assertEqual(result, expected)

    def test_10(self):
        solution_input = 200
        expected = 487067745
        result = solution_grandest_staircase.solution(solution_input)
        self.assertEqual(result, expected)
