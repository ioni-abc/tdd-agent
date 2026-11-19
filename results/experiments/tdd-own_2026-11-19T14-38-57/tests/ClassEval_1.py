import unittest


import unittest

import math

class AgentTest_calculate_circle_area(unittest.TestCase):

    def test_calculate_circle_area_1(self):
        # Docstring example: radius 2 -> 12.566370614359172
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(areaCalculator.calculate_circle_area(), 12.566370614359172)

    def test_calculate_circle_area_2(self):
        # Unit radius: area of a unit circle is pi
        areaCalculator = AreaCalculator(1)
        self.assertAlmostEqual(areaCalculator.calculate_circle_area(), math.pi)

    def test_calculate_circle_area_3(self):
        # Non-integer radius: area = pi * r^2 with r = 2.5
        areaCalculator = AreaCalculator(2.5)
        self.assertAlmostEqual(areaCalculator.calculate_circle_area(), math.pi * 2.5 ** 2)

    def test_calculate_circle_area_4(self):
        # Result is returned as a float
        areaCalculator = AreaCalculator(2)
        self.assertIsInstance(areaCalculator.calculate_circle_area(), float)

    def test_calculate_circle_area_5(self):
        # Area is based on self.radius: a fresh radius yields the new area
        areaCalculator = AreaCalculator(3)
        self.assertAlmostEqual(areaCalculator.calculate_circle_area(), 9 * math.pi)

import unittest

import math

class AgentTest_calculate_sphere_area(unittest.TestCase):

    def test_calculate_sphere_area_1(self):
        # Docstring example: radius 2 -> 50.26548245743669
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(areaCalculator.calculate_sphere_area(), 50.26548245743669)

    def test_calculate_sphere_area_2(self):
        # Unit radius: surface area of a unit sphere is 4 * pi
        areaCalculator = AreaCalculator(1)
        self.assertAlmostEqual(areaCalculator.calculate_sphere_area(), 4 * math.pi)

    def test_calculate_sphere_area_3(self):
        # Non-integer radius: area = 4 * pi * r^2 with r = 2.5
        areaCalculator = AreaCalculator(2.5)
        self.assertAlmostEqual(areaCalculator.calculate_sphere_area(), 4 * math.pi * 2.5 ** 2)

    def test_calculate_sphere_area_4(self):
        # Result is returned as a float
        areaCalculator = AreaCalculator(2)
        self.assertIsInstance(areaCalculator.calculate_sphere_area(), float)

    def test_calculate_sphere_area_5(self):
        # Area is based on self.radius: doubling the radius quadruples the area
        small = AreaCalculator(1.5).calculate_sphere_area()
        large = AreaCalculator(3).calculate_sphere_area()
        self.assertAlmostEqual(large, 4 * small)

import unittest

import math

class AgentTest_calculate_cylinder_area(unittest.TestCase):

    def test_calculate_cylinder_area_1(self):
        # Docstring example: radius 2, height 3 -> 62.83185307179586
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(areaCalculator.calculate_cylinder_area(3), 62.83185307179586)

    def test_calculate_cylinder_area_2(self):
        # Unit radius and unit height: 2*pi*1*(1+1) = 4 * pi
        areaCalculator = AreaCalculator(1)
        self.assertAlmostEqual(areaCalculator.calculate_cylinder_area(1), 4 * math.pi)

    def test_calculate_cylinder_area_3(self):
        # Non-integer radius and height: 2 * pi * r * (r + h) with r = 2.5, h = 4
        areaCalculator = AreaCalculator(2.5)
        self.assertAlmostEqual(areaCalculator.calculate_cylinder_area(4), 2 * math.pi * 2.5 * (2.5 + 4))

    def test_calculate_cylinder_area_4(self):
        # Result is returned as a float
        areaCalculator = AreaCalculator(2)
        self.assertIsInstance(areaCalculator.calculate_cylinder_area(3), float)

    def test_calculate_cylinder_area_5(self):
        # Area is based on self.radius: a fresh radius yields the new area
        # radius 3, height 3: 2 * pi * 3 * (3 + 3) = 36 * pi
        areaCalculator = AreaCalculator(3)
        self.assertAlmostEqual(areaCalculator.calculate_cylinder_area(3), 36 * math.pi)

import unittest

import math

class AgentTest_calculate_sector_area(unittest.TestCase):

    def test_calculate_sector_area_1(self):
        # Docstring example: radius 2, angle pi -> 0.5 * 2^2 * pi = 2 * pi = 6.283185307179586
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(areaCalculator.calculate_sector_area(math.pi), 6.283185307179586)

    def test_calculate_sector_area_2(self):
        # Full angle 2 * pi gives the whole circle: 0.5 * 1^2 * 2 * pi = pi
        areaCalculator = AreaCalculator(1)
        self.assertAlmostEqual(areaCalculator.calculate_sector_area(2 * math.pi), math.pi)

    def test_calculate_sector_area_3(self):
        # Non-integer radius and angle: 0.5 * r^2 * angle with r = 2.5, angle = 1.2
        areaCalculator = AreaCalculator(2.5)
        self.assertAlmostEqual(areaCalculator.calculate_sector_area(1.2), 0.5 * 2.5 ** 2 * 1.2)

    def test_calculate_sector_area_4(self):
        # Result is returned as a float
        areaCalculator = AreaCalculator(2)
        self.assertIsInstance(areaCalculator.calculate_sector_area(math.pi), float)

    def test_calculate_sector_area_5(self):
        # Area is based on self.radius: radius 3, angle pi -> 0.5 * 9 * pi = 4.5 * pi
        areaCalculator = AreaCalculator(3)
        self.assertAlmostEqual(areaCalculator.calculate_sector_area(math.pi), 4.5 * math.pi)

import unittest

import math

class AgentTest_calculate_annulus_area(unittest.TestCase):

    def test_calculate_annulus_area_1(self):
        # Docstring example: inner 2, outer 3 -> pi * (3^2 - 2^2) = 5 * pi = 15.707963267948966
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(areaCalculator.calculate_annulus_area(2, 3), 15.707963267948966)

    def test_calculate_annulus_area_2(self):
        # Equal inner and outer radii leave no ring, so the area is 0
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(areaCalculator.calculate_annulus_area(2.5, 2.5), 0)

    def test_calculate_annulus_area_3(self):
        # Non-integer radii: pi * (outer^2 - inner^2) with inner = 1.5, outer = 2.5
        areaCalculator = AreaCalculator(2)
        self.assertAlmostEqual(areaCalculator.calculate_annulus_area(1.5, 2.5), math.pi * (2.5 ** 2 - 1.5 ** 2))

    def test_calculate_annulus_area_4(self):
        # Result is returned as a float
        areaCalculator = AreaCalculator(2)
        self.assertIsInstance(areaCalculator.calculate_annulus_area(2, 3), float)

    def test_calculate_annulus_area_5(self):
        # Area is based on inner_radius and outer_radius, not on self.radius:
        # different instance radii give the same annulus area for (2, 3)
        small = AreaCalculator(1).calculate_annulus_area(2, 3)
        large = AreaCalculator(10).calculate_annulus_area(2, 3)
        self.assertAlmostEqual(small, large)
        self.assertAlmostEqual(small, 5 * math.pi)