import unittest
import importlib

class TestProjectITSCertification(unittest.TestCase):
    def test_01(self):
        self.assertEqual(answers.answer_01, 3)
    def test_02(self):
        self.assertEqual(answers.answer_02, 2)
    def test_03(self):
        self.assertIn(2, answers.answer_03)
        self.assertIn(4, answers.answer_03)
    def test_04(self):
        self.assertEqual(answers.answer_04["A"], 1)
        self.assertEqual(answers.answer_04["B"], 2)
        self.assertEqual(answers.answer_04["C"], 3)
        self.assertEqual(answers.answer_04["D"], 4)
        self.assertEqual(answers.answer_04["E"], 3)
    def test_05(self):
        self.assertEqual(answers.answer_05, 1)

chapter_name = "IT Specialist Certification - Python"
answers = importlib.import_module("answers")
suite = unittest.TestLoader().loadTestsFromTestCase(TestProjectITSCertification)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print(f"您在「{chapter_name}」章節的 {number_of_test_runs} 道練習題中答對了 {number_of_successes} 題。")