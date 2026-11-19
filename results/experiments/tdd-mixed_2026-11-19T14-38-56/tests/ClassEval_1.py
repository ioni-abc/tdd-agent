import unittest



class AreaCalculatorTestCalculateCircleArea(unittest.TestCase):
    def test_calculate_circle_area(self):
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(12.56, areaCalculator.calculate_circle_area(), delta=0.01)

    def test_calculate_circle_area_2(self):
        areaCalculator = AreaCalculator(2.5)
        self.assertAlmostEqual(19.63, areaCalculator.calculate_circle_area(), delta=0.01)

    def test_calculate_circle_area_3(self):
        areaCalculator = AreaCalculator(2000)
        self.assertAlmostEqual(12566370.61, areaCalculator.calculate_circle_area(), delta=0.01)

import math

import unittest

class AgentTest_calculate_circle_area(unittest.TestCase):
    def test_calculate_circle_area_1(self):
        areaCalculator = AreaCalculator(1)
        self.assertAlmostEqual(math.pi, areaCalculator.calculate_circle_area(), places=7)

    def test_calculate_circle_area_2(self):
        areaCalculator = AreaCalculator(0)
        self.assertEqual(0, areaCalculator.calculate_circle_area())

class AreaCalculatorTestCalculateSphereArea(unittest.TestCase):
    def test_calculate_sphere_area(self):
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(50.27, areaCalculator.calculate_sphere_area(), delta=0.01)

    def test_calculate_sphere_area_2(self):
        areaCalculator = AreaCalculator(2.5)
        self.assertAlmostEqual(19.63, areaCalculator.calculate_circle_area(), delta=0.01)

    def test_calculate_sphere_area_3(self):
        areaCalculator = AreaCalculator(2000)
        self.assertAlmostEqual(12566370.61, areaCalculator.calculate_circle_area(), delta=0.01)

import math

import unittest

class AgentTest_calculate_sphere_area(unittest.TestCase):
    def test_calculate_sphere_area_1(self):
        areaCalculator = AreaCalculator(1)
        self.assertAlmostEqual(4 * math.pi, areaCalculator.calculate_sphere_area(), places=7)

    def test_calculate_sphere_area_2(self):
        areaCalculator = AreaCalculator(0.5)
        self.assertAlmostEqual(math.pi, areaCalculator.calculate_sphere_area(), places=7)

class AreaCalculatorTestCalculateCylinderArea(unittest.TestCase):
    def test_calculate_cylinder_area(self):
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(50.27, areaCalculator.calculate_cylinder_area(2), delta=0.01)

    def test_calculate_cylinder_area_2(self):
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(25.13, areaCalculator.calculate_cylinder_area(0), delta=0.01)

    def test_calculate_cylinder_area_3(self):
        areaCalculator = AreaCalculator(0)
        self.assertAlmostEqual(0, areaCalculator.calculate_cylinder_area(2000), delta=0.01)

import math

class AgentTest_calculate_cylinder_area(unittest.TestCase):
    def test_calculate_cylinder_area_1(self):
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(62.83185307179586, areaCalculator.calculate_cylinder_area(3), places=7)

    def test_calculate_cylinder_area_2(self):
        areaCalculator = AreaCalculator(0.5)
        self.assertAlmostEqual(3.5 * math.pi, areaCalculator.calculate_cylinder_area(3), places=7)

class AreaCalculatorTestCalculateSectorArea(unittest.TestCase):
    def test_calculate_sector_area(self):
        areaCalculator = AreaCalculator(1.5)
        self.assertAlmostEqual(3.53, areaCalculator.calculate_sector_area(math.pi), delta=0.01)

    def test_calculate_sector_area_2(self):
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(3.14, areaCalculator.calculate_sector_area(math.pi/2), delta=0.01)

    def test_calculate_sector_area_3(self):
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(0, areaCalculator.calculate_sector_area(0), delta=0.01)

import math

import unittest

class AgentTest_calculate_sector_area(unittest.TestCase):
    def test_calculate_sector_area_1(self):
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(4 * math.pi, areaCalculator.calculate_sector_area(2 * math.pi), places=7)

    def test_calculate_sector_area_2(self):
        areaCalculator = AreaCalculator(3)
        self.assertAlmostEqual(4.5, areaCalculator.calculate_sector_area(1), places=7)

class AreaCalculatorTestCalculateAnnulusArea(unittest.TestCase):
    def test_calculate_annulus_area(self):
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(25.128, areaCalculator.calculate_annulus_area(1, 3), delta=0.01)

    def test_calculate_annulus_area_2(self):
        areaCalculator = AreaCalculator(2.5)
        self.assertAlmostEqual(0, areaCalculator.calculate_annulus_area(3, 3), delta=0.01)

    def test_calculate_annulus_area_3(self):
        areaCalculator = AreaCalculator(2000)
        self.assertAlmostEqual(3.14, areaCalculator.calculate_annulus_area(0, 1), delta=0.01)

import math

import unittest

class AgentTest_calculate_annulus_area(unittest.TestCase):
    def test_calculate_annulus_area_1(self):
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(5 * math.pi, areaCalculator.calculate_annulus_area(2, 3), places=7)

    def test_calculate_annulus_area_2(self):
        areaCalculator = AreaCalculator(100)
        self.assertAlmostEqual(4 * math.pi, areaCalculator.calculate_annulus_area(1.5, 2.5), places=7)