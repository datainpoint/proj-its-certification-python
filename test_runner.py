import unittest
import importlib

class TestProjectITSCertification(unittest.TestCase):
    def test_01(self):
        self.assertEqual(answers.answer_01, 3)
    def test_02(self):
        self.assertEqual(answers.answer_02, 2)
    def test_03(self):
        self.assertEqual(answers.answer_03, {2, 4})
    def test_04(self):
        self.assertEqual(answers.answer_04["A"], 1)
        self.assertEqual(answers.answer_04["B"], 2)
        self.assertEqual(answers.answer_04["C"], 3)
        self.assertEqual(answers.answer_04["D"], 4)
        self.assertEqual(answers.answer_04["E"], 3)
    def test_05(self):
        self.assertEqual(answers.answer_05, 1)
    def test_06(self):
        self.assertEqual(answers.answer_06, 1)
    def test_07(self):
        self.assertEqual(answers.answer_07, {1, 2})
    def test_08(self):
        self.assertEqual(answers.answer_08, 2)
    def test_09(self):
        self.assertEqual(answers.answer_09, 2)
    def test_10(self):
        self.assertEqual(answers.answer_10, 1)
    def test_11(self):
        self.assertEqual(answers.answer_11, 1)
    def test_12(self):
        self.assertEqual(answers.answer_12, 1)
    def test_13(self):
        self.assertEqual(answers.answer_13, {3, 4})
    def test_14(self):
        self.assertEqual(answers.answer_14, 3)
    def test_15(self):
        self.assertEqual(answers.answer_15["A"], 1)
        self.assertEqual(answers.answer_15["B"], 2)
        self.assertEqual(answers.answer_15["C"], 3)
    def test_16(self):
        self.assertEqual(answers.answer_16["A"], 1)
        self.assertEqual(answers.answer_16["B"], 6)
        self.assertEqual(answers.answer_16["C"], 9)
    def test_17(self):
        self.assertEqual(answers.answer_17, 2)
    def test_18(self):
        self.assertEqual(answers.answer_18["A"], 2)
        self.assertEqual(answers.answer_18["B"], 1)
        self.assertEqual(answers.answer_18["C"], 1)
    def test_19(self):
        self.assertEqual(answers.answer_19["A"], 3)
        self.assertEqual(answers.answer_19["B"], 2)
        self.assertEqual(answers.answer_19["C"], 1)
    def test_20(self):
        self.assertEqual(answers.answer_20["A"], 2)
        self.assertEqual(answers.answer_20["B"], 1)
        self.assertEqual(answers.answer_20["C"], 2)
        self.assertEqual(answers.answer_20["D"], 2)
    def test_21(self):
        self.assertEqual(answers.answer_21, 2)
    def test_22(self):
        self.assertEqual(answers.answer_22, 3)
    def test_23(self):
        self.assertEqual(answers.answer_23["A"], 1)
        self.assertEqual(answers.answer_23["B"], 1)
        self.assertEqual(answers.answer_23["C"], 2)
        self.assertEqual(answers.answer_23["D"], 2)
    def test_24(self):
        self.assertEqual(answers.answer_24["A"], 4)
        self.assertEqual(answers.answer_24["B"], 8)
    def test_25(self):
        self.assertEqual(answers.answer_25["A"], 3)
        self.assertEqual(answers.answer_25["B"], 6)
        self.assertEqual(answers.answer_25["C"], 2)
        self.assertEqual(answers.answer_25["D"], 1)
    def test_26(self):
        self.assertEqual(answers.answer_26, {2, 4})
    def test_27(self):
        self.assertEqual(answers.answer_27, 3)
    def test_28(self):
        self.assertEqual(answers.answer_28["A"], 1)
        self.assertEqual(answers.answer_28["B"], 5)
    def test_29(self):
        self.assertEqual(answers.answer_29["A"], 3)
        self.assertEqual(answers.answer_29["B"], 8)
        self.assertEqual(answers.answer_29["C"], 10)
    def test_30(self):
        self.assertEqual(answers.answer_30, 1)

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