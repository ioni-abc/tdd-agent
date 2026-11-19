import unittest


import unittest

class AgentTest_interpolate_1d(unittest.TestCase):

    def assertListAlmostEqual(self, actual, expected):
        self.assertIsInstance(actual, list)
        self.assertEqual(len(actual), len(expected))
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(a, e)

    def test_interpolate_1d_1(self):
        # Docstring example
        result = Interpolation.interpolate_1d([1, 2, 3], [1, 2, 3], [1.5, 2.5])
        self.assertListAlmostEqual(result, [1.5, 2.5])

    def test_interpolate_1d_2(self):
        # Interpolating at the data x-coordinates returns the original y-values
        result = Interpolation.interpolate_1d([1, 2, 3], [10, 20, 30], [1, 2, 3])
        self.assertListAlmostEqual(result, [10, 20, 30])

    def test_interpolate_1d_3(self):
        # Linear data y = 2x + 1 with non-integer interpolation points
        result = Interpolation.interpolate_1d([0, 1, 2, 3], [1, 3, 5, 7], [0.25, 2.75])
        self.assertListAlmostEqual(result, [1.5, 6.5])

    def test_interpolate_1d_4(self):
        # Non-uniform spacing: segment [1, 4] has slope 10
        result = Interpolation.interpolate_1d([0, 1, 4], [0, 10, 40], [0.5, 2.0, 3.0])
        self.assertListAlmostEqual(result, [5.0, 20.0, 30.0])

    def test_interpolate_1d_5(self):
        # Output is a list with one y-value per x_interp point, in the same order
        x_interp = [2.5, 1.5, 0.5, 1.0]
        result = Interpolation.interpolate_1d([0, 1, 2], [0, 4, 8], x_interp)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), len(x_interp))
        self.assertListAlmostEqual(result, [10.0, 6.0, 2.0, 4.0])

import unittest

class AgentTest_interpolate_2d(unittest.TestCase):

    def assertListAlmostEqual(self, actual, expected):
        self.assertIsInstance(actual, list)
        self.assertEqual(len(actual), len(expected))
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(a, e)

    def test_interpolate_2d_1(self):
        # Docstring example
        result = Interpolation.interpolate_2d(
            [1, 2, 3], [1, 2, 3], [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [1.5, 2.5], [1.5, 2.5])
        self.assertListAlmostEqual(result, [3.0, 7.0])

    def test_interpolate_2d_2(self):
        # Interpolating at grid nodes returns the original z-values
        # z[i][j] corresponds to y[i] and x[j]: (x=1, y=2) -> z[1][0] = 4, (x=3, y=3) -> z[2][2] = 9
        result = Interpolation.interpolate_2d(
            [1, 2, 3], [1, 2, 3], [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [1, 3], [2, 3])
        self.assertListAlmostEqual(result, [4, 9])

    def test_interpolate_2d_3(self):
        # Linear data z = x + 2y is reproduced exactly by bilinear interpolation
        xs = [0, 1, 2]
        ys = [0, 1, 2]
        z = [[xj + 2 * yi for xj in xs] for yi in ys]
        result = Interpolation.interpolate_2d(
            xs, ys, z, [0.5, 1.25], [1.5, 0.75])
        self.assertListAlmostEqual(result, [3.5, 2.75])

    def test_interpolate_2d_4(self):
        # Output has one z-value per (x_interp, y_interp) pair, in the same order as the inputs
        result = Interpolation.interpolate_2d(
            [1, 2, 3], [1, 2, 3], [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [2.5, 1.5], [2.5, 1.5])
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        self.assertListAlmostEqual(result, [7.0, 3.0])

    def test_interpolate_2d_5(self):
        # Non-square grid: x has 3 values, y has 2 values, so z has 2 rows of 3 values
        # z[i][j] corresponds to y[i] and x[j]
        result = Interpolation.interpolate_2d(
            [1, 2, 3], [1, 2], [[1, 2, 3], [4, 5, 6]],
            [2.5, 3.0], [1.5, 1.0])
        self.assertListAlmostEqual(result, [4.0, 3.0])