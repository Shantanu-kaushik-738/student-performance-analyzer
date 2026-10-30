import unittest

from main import (
    calculate_total,
    calculate_percentage,
    check_result,
    calculate_grade,
    find_topper,
    calculate_pass_percentage,
    calculate_subject_averages,
    analyze_student,
)


class TestStudentPerformanceAnalyzer(unittest.TestCase):
    def test_calculate_total(self):
        self.assertEqual(calculate_total([80, 70, 90]), 240)

    def test_calculate_percentage(self):
        self.assertEqual(calculate_percentage([80, 70, 90]), 80)

    def test_pass_when_every_subject_meets_threshold(self):
        self.assertTrue(check_result([33, 50, 70]))

    def test_fail_when_any_subject_is_below_threshold(self):
        self.assertFalse(check_result([90, 32, 80]))

    def test_grade_boundaries(self):
        self.assertEqual(calculate_grade(90), "A")
        self.assertEqual(calculate_grade(75), "B")
        self.assertEqual(calculate_grade(60), "C")
        self.assertEqual(calculate_grade(33), "D")
        self.assertEqual(calculate_grade(32.99), "F")

    def test_empty_topper(self):
        self.assertIsNone(find_topper([]))

    def test_pass_percentage(self):
        data = [
            {"name": "A", "marks": [80, 70, 90]},
            {"name": "B", "marks": [20, 80, 90]},
        ]
        self.assertEqual(calculate_pass_percentage(data), 50)

    def test_subject_averages(self):
        data = [
            {"name": "A", "marks": [80, 60]},
            {"name": "B", "marks": [100, 80]},
        ]
        self.assertEqual(
            calculate_subject_averages(data, ["Python", "DBMS"]),
            {"Python": 90.0, "DBMS": 70.0},
        )

    def test_failed_student_gets_f_grade(self):
        report = analyze_student({"name": "Rahul", "marks": [32, 45, 28]})
        self.assertEqual(report["result"], "Fail")
        self.assertEqual(report["grade"], "F")

    def test_invalid_marks_raise_error(self):
        with self.assertRaises(ValueError):
            calculate_total([80, 120, 90])


if __name__ == "__main__":
    unittest.main()
