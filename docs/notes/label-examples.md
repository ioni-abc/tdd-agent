# Two labels explained with a real example: `no_method_info` and `other_inconsistency`

Both examples are from `ClassEval_1` (class `AreaCalculator`). Labels are in `results/analysis/benchmark_labels.csv` (`scripts/label_tests.py`).

## `no_method_info`: 108 of 2196 tests, no LLM call

**Rule:** the test's class is in no `methods_info[i]["test_class"]`, so the test belongs to no single method and there is no docstring to compare it with.

**Example:** `AreaCalculatorTestCalculateMain.test_main`. The `methods_info[i]["test_class"]` values of `ClassEval_1` are `AreaCalculatorTestCalculateCircleArea`, `...SphereArea`, `...CylinderArea`, `...SectorArea` and `...AnnulusArea`. `AreaCalculatorTestCalculateMain` is not one of them.

```python
def test_main(self):
    areaCalculator = AreaCalculator(2)
    self.assertAlmostEqual(12.56, areaCalculator.calculate_circle_area(), delta=0.01)
    self.assertAlmostEqual(50.27, areaCalculator.calculate_sphere_area(), delta=0.01)
    self.assertAlmostEqual(50.27, areaCalculator.calculate_cylinder_area(2), delta=0.01)
    self.assertAlmostEqual(6.28, areaCalculator.calculate_sector_area(math.pi), delta=0.01)
    self.assertAlmostEqual(25.128, areaCalculator.calculate_annulus_area(1, 3), delta=0.01)
```

It calls five methods at once, so no single docstring can be compared with it. It is still scored in every run (in the cross-check it is the `no_method_info` row).

## `other_inconsistency`: 58 of the 2088 judged tests

**Rule:** the test and the docstring do not fit together, in a way that is neither `unstated` (docstring silent) nor `contradicts` (docstring says something else). The common case is a test filed under one method that tests a different one.

**Example:** `AreaCalculatorTestCalculateSphereArea.test_calculate_sphere_area_2`, filed under `calculate_sphere_area`:

```python
def test_calculate_sphere_area_2(self):
    areaCalculator = AreaCalculator(2.5)
    self.assertAlmostEqual(19.63, areaCalculator.calculate_circle_area(), delta=0.01)
```

The docstring of `calculate_sphere_area` (`methods_info[i]["method_description"]`):

```python
"""
calculate the area of sphere based on self.radius
:return: area of sphere, float
>>> areaCalculator = AreaCalculator(2)
>>> areaCalculator.calculate_sphere_area()
50.26548245743669
"""
```

The test never calls `calculate_sphere_area`; it calls `calculate_circle_area`. The judge's label: `other_inconsistency`, reason: "Wrong method under test: the test is filed as a sphere-area test but calls calculate_circle_area, which the docstring of calculate_sphere_area does not describe." Tests 3, 4 and 5 of the same class have the same problem.
