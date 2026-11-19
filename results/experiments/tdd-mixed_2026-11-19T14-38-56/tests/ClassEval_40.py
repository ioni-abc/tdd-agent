import unittest




class FitnessTrackerTestGetBMI(unittest.TestCase):
    def test_get_BMI(self):
        fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        self.assertEqual(fitnessTracker.get_BMI(), 21.604938271604937)

    def test_get_BMI_2(self):
        fitnessTracker = FitnessTracker(1.8, 50, 20, "male")
        self.assertEqual(fitnessTracker.get_BMI(), 15.432098765432098)

    def test_get_BMI_3(self):
        fitnessTracker = FitnessTracker(1.72, 53, 20, "male")
        self.assertEqual(fitnessTracker.get_BMI(), 17.915089237425637)

import unittest

class AgentTest_get_BMI(unittest.TestCase):
    def test_get_BMI_1(self):
        fitnessTracker = FitnessTracker(1.6, 60, 30, "female")
        self.assertAlmostEqual(fitnessTracker.get_BMI(), 23.4375, places=7)

    def test_get_BMI_2(self):
        fitnessTracker = FitnessTracker(1.5, 45, 40, "female")
        self.assertAlmostEqual(fitnessTracker.get_BMI(), 20.0, places=7)

class FitnessTrackerTestConditionJudge(unittest.TestCase):
    def test_condition_judge(self):
        fitnessTracker = FitnessTracker(1.8, 45, 20, "female")
        self.assertEqual(fitnessTracker.condition_judge(), -1)

    def test_condition_judge_2(self):
        fitnessTracker = FitnessTracker(1.72, 80, 22, "female")
        self.assertEqual(fitnessTracker.condition_judge(), 1)

    def test_condition_judge_3(self):
        fitnessTracker = FitnessTracker(1.72, 53, 22, "male")
        self.assertEqual(fitnessTracker.condition_judge(), -1)

import unittest

class AgentTest_condition_judge(unittest.TestCase):
    def test_condition_judge_1(self):
        # Male with BMI about 22.9, inside the male normal range 20-25
        fitnessTracker = FitnessTracker(1.75, 70, 25, "male")
        self.assertEqual(fitnessTracker.condition_judge(), 0)

    def test_condition_judge_2(self):
        # Female with BMI about 21.5, inside the female normal range 19-24
        fitnessTracker = FitnessTracker(1.6, 55, 30, "female")
        self.assertEqual(fitnessTracker.condition_judge(), 0)

class FitnessTrackerTestCaculateCalorieIntake(unittest.TestCase):
    def test_calculate_calorie_intake(self):
        fitnessTracker = FitnessTracker(1.8, 70, 20, "female")
        self.assertEqual(fitnessTracker.calculate_calorie_intake(), 630.3499999999999)

    def test_calculate_calorie_intake_2(self):
        fitnessTracker = FitnessTracker(1.72, 80, 22, "female")
        self.assertEqual(fitnessTracker.calculate_calorie_intake(), 647.6999999999999)

    def test_calculate_calorie_intake_3(self):
        fitnessTracker = FitnessTracker(1.72, 53, 22, "male")
        self.assertEqual(fitnessTracker.calculate_calorie_intake(), 697.2)

import unittest

class AgentTest_calculate_calorie_intake(unittest.TestCase):
    def test_calculate_calorie_intake_1(self):
        # Docstring example: male, 1.8 m, 70 kg, age 20 -> BMR 616.25, thin multiplier 1.6
        fitnessTracker = FitnessTracker(1.8, 70, 20, "male")
        self.assertAlmostEqual(fitnessTracker.calculate_calorie_intake(), 986.0, places=7)

    def test_calculate_calorie_intake_2(self):
        # Female, 1.8 m, 45 kg, age 20 -> BMR 200.25, too thin (condition -1), multiplier 1.6
        fitnessTracker = FitnessTracker(1.8, 45, 20, "female")
        self.assertAlmostEqual(fitnessTracker.calculate_calorie_intake(), 320.4, places=7)