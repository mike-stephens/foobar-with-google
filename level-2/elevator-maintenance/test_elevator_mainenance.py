import solution_elevator_maintenance
import unittest


class TestElevatorMaintenance(unittest.TestCase):

    def test_1(self):
        solution_input = [
            "1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
        expected = [
            "0.1", "1.1.1", "1.2", "1.2.1", "1.11", "2", "2.0", "2.0.0"]
        result = solution_elevator_maintenance.solution(solution_input)
        self.assertEqual(result, expected)

    def test_2(self):
        solution_input = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]
        expected = ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]
        result = solution_elevator_maintenance.solution(solution_input)
        self.assertEqual(result, expected)
