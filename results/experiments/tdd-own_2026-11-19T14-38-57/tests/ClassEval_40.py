import unittest


import unittest

class AgentTest_get_BMI(unittest.TestCase):

    def test_get_BMI_1(self):
        tracker = FitnessTracker(1.8, 70, 20, "male")
        self.assertAlmostEqual(tracker.get_BMI(), 21.604938271604937, places=7)

    def test_get_BMI_2(self):
        tracker = FitnessTracker(1.6, 50, 25, "female")
        self.assertAlmostEqual(tracker.get_BMI(), 19.53125, places=7)

    def test_get_BMI_3(self):
        tracker = FitnessTracker(2.0, 100, 40, "male")
        self.assertAlmostEqual(tracker.get_BMI(), 25.0, places=7)

    def test_get_BMI_4(self):
        tracker = FitnessTracker(2, 80, 30, "female")
        bmi = tracker.get_BMI()
        self.assertIsInstance(bmi, float)
        self.assertAlmostEqual(bmi, 20.0, places=7)

    def test_get_BMI_5(self):
        male = FitnessTracker(1.75, 68, 22, "male")
        female = FitnessTracker(1.75, 68, 55, "female")
        self.assertAlmostEqual(male.get_BMI(), female.get_BMI(), places=7)
        self.assertAlmostEqual(male.get_BMI(), 68 / (1.75 ** 2), places=7)

import unittest

class AgentTest_condition_judge(unittest.TestCase):

    def test_condition_judge_1(self):
        # male, BMI = 100 / 1.75^2 = 32.65 (above 25) -> too fat
        tracker = FitnessTracker(1.75, 100, 30, "male")
        self.assertEqual(tracker.condition_judge(), 1)

    def test_condition_judge_2(self):
        # male, BMI = 50 / 1.8^2 = 15.43 (below 20) -> too thin
        tracker = FitnessTracker(1.8, 50, 30, "male")
        self.assertEqual(tracker.condition_judge(), -1)

    def test_condition_judge_3(self):
        # male, BMI = 70 / 1.75^2 = 22.86 (within 20-25) -> normal
        tracker = FitnessTracker(1.75, 70, 30, "male")
        self.assertEqual(tracker.condition_judge(), 0)

    def test_condition_judge_4(self):
        # female, BMI = 63 / 1.6^2 = 24.61 (above female upper limit 24) -> too fat
        tracker = FitnessTracker(1.6, 63, 30, "female")
        self.assertEqual(tracker.condition_judge(), 1)

    def test_condition_judge_5(self):
        # female, BMI = 50 / 1.6^2 = 19.53 (within female 19-24) -> normal
        tracker = FitnessTracker(1.6, 50, 30, "female")
        self.assertEqual(tracker.condition_judge(), 0)

import unittest

class AgentTest_calculate_calorie_intake(unittest.TestCase):

    def test_calculate_calorie_intake_1(self):
        # Docstring example: male, BMR = 10*70 + 6.25*1.8 - 5*20 + 5 = 616.25
        # BMI = 21.6 is too thin (below 20 is not the case, but condition is -1 per spec example), factor 1.6
        tracker = FitnessTracker(1.8, 70, 20, "male")
        self.assertAlmostEqual(tracker.calculate_calorie_intake(), 986.0, places=7)

    def test_calculate_calorie_intake_2(self):
        # male, BMR = 10*100 + 6.25*1.75 - 5*30 + 5 = 865.9375
        # too fat (condition 1), factor 1.2 -> 1039.125
        tracker = FitnessTracker(1.75, 100, 30, "male")
        self.assertAlmostEqual(tracker.calculate_calorie_intake(), 1039.125, places=7)

    def test_calculate_calorie_intake_3(self):
        # male, BMR = 10*70 + 6.25*1.75 - 5*30 + 5 = 565.9375
        # normal (condition 0), factor 1.4 -> 792.3125
        tracker = FitnessTracker(1.75, 70, 30, "male")
        self.assertAlmostEqual(tracker.calculate_calorie_intake(), 792.3125, places=7)

    def test_calculate_calorie_intake_4(self):
        # female, BMR = 10*50 + 6.25*1.6 - 5*30 - 161 = 199.0
        # normal (condition 0), factor 1.4 -> 278.6
        tracker = FitnessTracker(1.6, 50, 30, "female")
        self.assertAlmostEqual(tracker.calculate_calorie_intake(), 278.6, places=7)

    def test_calculate_calorie_intake_5(self):
        # female, BMR = 10*63 + 6.25*1.6 - 5*30 - 161 = 329.0
        # too fat (condition 1), factor 1.2 -> 394.8
        tracker = FitnessTracker(1.6, 63, 30, "female")
        self.assertAlmostEqual(tracker.calculate_calorie_intake(), 394.8, places=7)