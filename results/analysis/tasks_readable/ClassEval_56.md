# ClassEval_56

## Skeleton (what the agent sees)

```python
class MetricsCalculator:
    """
    The class calculates precision, recall, F1 score, and accuracy based on predicted and true labels.
    """

    def __init__(self):
        """
        Initialize the number of all four samples to 0
        """
        self.true_positives = 0
        self.false_positives = 0
        self.false_negatives = 0
        self.true_negatives = 0


    def update(self, predicted_labels, true_labels):
        """
        Update the number of all four samples(true_positives, false_positives, false_negatives, true_negatives)
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: None, change the number of corresponding samples
        >>> mc = MetricsCalculator()
        >>> mc.update([1, 1, 0, 0], [1, 0, 0, 1])
        (self.true_positives, self.false_positives, self.false_negatives, self.true_negatives) = (1, 1, 1, 1)
        """


    def precision(self, predicted_labels, true_labels):
        """
        Calculate precision
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.precision([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """


    def recall(self, predicted_labels, true_labels):
        """
        Calculate recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.recall([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """


    def f1_score(self, predicted_labels, true_labels):
        """
        Calculate f1 score, which is the harmonic mean of precision and recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.f1_score([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """


    def accuracy(self, predicted_labels, true_labels):
        """
        Calculate accuracy
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>>mc.accuracy([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
```

## Method `update`

### Docstring

```python
def update(self, predicted_labels, true_labels):
        """
        Update the number of all four samples(true_positives, false_positives, false_negatives, true_negatives)
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: None, change the number of corresponding samples
        >>> mc = MetricsCalculator()
        >>> mc.update([1, 1, 0, 0], [1, 0, 0, 1])
        (self.true_positives, self.false_positives, self.false_negatives, self.true_negatives) = (1, 1, 1, 1)
        """
```

### Reference code (`solution_code`)

```python
def update(self, predicted_labels, true_labels):
        for predicted, true in zip(predicted_labels, true_labels):
            if predicted == 1 and true == 1:
                self.true_positives += 1
            elif predicted == 1 and true == 0:
                self.false_positives += 1
            elif predicted == 0 and true == 1:
                self.false_negatives += 1
            elif predicted == 0 and true == 0:
                self.true_negatives += 1
```

### Tests (`MetricsCalculatorTestUpdate`)

**test_update_1**: `stated`
- reason: The docstring names the four counters and its example gives (1, 1, 1, 1) for the same inputs, so a programmer following it would count each predicted/true pair into the standard confusion-matrix bucket and pass.

```python
def test_update_1(self):
    mc = MetricsCalculator()
    self.assertEqual((mc.true_positives, mc.false_positives, mc.false_negatives, mc.true_negatives), (0, 0, 0, 0))
    mc.update([1, 1, 0, 0], [1, 0, 0, 1])
    self.assertEqual((mc.true_positives, mc.false_positives, mc.false_negatives, mc.true_negatives), (1, 1, 1, 1))
```

**test_update_2**: `stated`
- reason: The docstring names the four counters and gives an example, so a programmer would count predicted/true pairs into the standard confusion-matrix categories, which yields the (1, 2, 1, 0) the test expects.

```python
def test_update_2(self):
    mc = MetricsCalculator()
    self.assertEqual((mc.true_positives, mc.false_positives, mc.false_negatives, mc.true_negatives), (0, 0, 0, 0))
    mc.update([1, 1, 1, 0], [1, 0, 0, 1])
    self.assertEqual((mc.true_positives, mc.false_positives, mc.false_negatives, mc.true_negatives), (1, 2, 1, 0))
```

**test_update_3**: `stated`
- reason: The docstring's example shows that predicted 1 with true 1 counts as a true positive, predicted 1 with true 0 as a false positive, and so on, and the test uses the same convention and accumulates across calls, which the docstring's "update the number" wording supports.

```python
def test_update_3(self):
    mc = MetricsCalculator()
    self.assertEqual((mc.true_positives, mc.false_positives, mc.false_negatives, mc.true_negatives), (0, 0, 0, 0))
    mc.update([1, 1, 0, 1], [1, 0, 0, 1])
    self.assertEqual((mc.true_positives, mc.false_positives, mc.false_negatives, mc.true_negatives), (2, 1, 0, 1))
```

**test_update_4**: `stated`
- reason: A programmer applying the standard confusion-matrix meaning of the four counters (predicted 1 with true 1 is a true positive, predicted 1 with true 0 is a false positive, and so on) would produce the test's expected (2, 0, 1, 1).

```python
def test_update_4(self):
    mc = MetricsCalculator()
    self.assertEqual((mc.true_positives, mc.false_positives, mc.false_negatives, mc.true_negatives), (0, 0, 0, 0))
    mc.update([1, 1, 0, 0], [1, 1, 0, 1])
    self.assertEqual((mc.true_positives, mc.false_positives, mc.false_negatives, mc.true_negatives), (2, 0, 1, 1))
```

**test_update_5**: `stated`
- reason: The docstring's example gives the standard confusion-matrix mapping (predicted 1 with true 1 is a true positive, predicted 1 with true 0 is a false positive, and so on), which a programmer would apply to this test's input and produce (1, 1, 2, 0).

```python
def test_update_5(self):
    mc = MetricsCalculator()
    self.assertEqual((mc.true_positives, mc.false_positives, mc.false_negatives, mc.true_negatives), (0, 0, 0, 0))
    mc.update([1, 1, 0, 0], [1, 0, 1, 1])
    self.assertEqual((mc.true_positives, mc.false_positives, mc.false_negatives, mc.true_negatives), (1, 1, 2, 0))
```

## Method `precision`

### Docstring

```python
def precision(self, predicted_labels, true_labels):
        """
        Calculate precision
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.precision([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
```

### Reference code (`solution_code`)

```python
def precision(self, predicted_labels, true_labels):
        self.update(predicted_labels, true_labels)
        if self.true_positives + self.false_positives == 0:
            return 0.0
        return self.true_positives / (self.true_positives + self.false_positives)
```

### Tests (`MetricsCalculatorTestPrecision`)

**test_precision_1**: `stated`
- reason: The docstring gives the standard precision definition (true positives over true positives plus false positives) and an example that yields 0.5, which is the value the test expects for these inputs.

```python
def test_precision_1(self):
    mc = MetricsCalculator()
    temp = mc.precision([1, 1, 0, 0], [1, 0, 0, 1])
    self.assertEqual(temp, 0.5)
```

**test_precision_2**: `stated`
- reason: The docstring's example and standard binary precision (true positives over predicted positives, with 1 as the positive class) give 1/3 for this input, which matches the test's expected value.

```python
def test_precision_2(self):
    mc = MetricsCalculator()
    temp = mc.precision([1, 1, 1, 0], [1, 0, 0, 1])
    self.assertAlmostEqual(temp, 0.3333333333333333)
```

**test_precision_3**: `stated`
- reason: The docstring's example (precision of [1,1,0,0] against [1,0,0,1] is 0.5) fixes the formula as true positives divided by predicted positives, and the test's case (2 true positives, 1 false positive, giving 2/3) follows that same rule.

```python
def test_precision_3(self):
    mc = MetricsCalculator()
    temp = mc.precision([1, 1, 0, 1], [1, 0, 0, 1])
    self.assertAlmostEqual(temp, 0.6666666666666666)
```

**test_precision_4**: `stated`
- reason: A programmer following the docstring's precision definition and its example (positive class 1, precision as true positives over predicted positives) would compute 2/(2+0) = 1.0 for this input, matching the test.

```python
def test_precision_4(self):
    mc = MetricsCalculator()
    temp = mc.precision([1, 1, 0, 0], [1, 1, 0, 1])
    self.assertAlmostEqual(temp, 1.0)
```

**test_precision_5**: `stated`
- reason: The docstring's own example and the standard definition of precision (true positives over true plus false positives, with label 1 as positive) give 0.5 for this input, so a programmer following the docstring would pass the test.

```python
def test_precision_5(self):
    mc = MetricsCalculator()
    temp = mc.precision([1, 1, 0, 0], [1, 0, 1, 1])
    self.assertAlmostEqual(temp, 0.5)
```

**test_precision_6**: `unstated`
- reason: The docstring gives no value for precision when the model predicts no positive labels, so the zero-denominator case is left open and a programmer could reasonably raise an error or return NaN instead of 0.0.
- missing: The docstring should say what precision returns when there are no predicted positives (true positives plus false positives equal zero), e.g. whether it returns 0.0 or raises an error.

```python
def test_precision_6(self):
    mc = MetricsCalculator()
    temp = mc.precision([0, 0, 0, 0], [1, 0, 1, 1])
    self.assertAlmostEqual(temp, 0.0)
```

## Method `recall`

### Docstring

```python
def recall(self, predicted_labels, true_labels):
        """
        Calculate recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.recall([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
```

### Reference code (`solution_code`)

```python
def recall(self, predicted_labels, true_labels):
        self.update(predicted_labels, true_labels)
        if self.true_positives + self.false_negatives == 0:
            return 0.0
        return self.true_positives / (self.true_positives + self.false_negatives)
```

### Tests (`MetricsCalculatorTestRecall`)

**test_recall_1**: `stated`
- reason: The docstring's doctest uses the same inputs and expected value (0.5) as the test, so a programmer following it would get the test's result.

```python
def test_recall_1(self):
    mc = MetricsCalculator()
    temp = mc.recall([1, 1, 0, 0], [1, 0, 0, 1])
    self.assertEqual(temp, 0.5)
```

**test_recall_2**: `stated`
- reason: The docstring's own example (recall = true positives over all actual positives, with label 1 as the positive class) gives the same 0.5 expected by this test, so a programmer following it would pass.

```python
def test_recall_2(self):
    mc = MetricsCalculator()
    temp = mc.recall([1, 1, 1, 0], [1, 0, 0, 1])
    self.assertEqual(temp, 0.5)
```

**test_recall_3**: `stated`
- reason: The docstring defines recall as the standard ratio of true positives to actual positives, and the test's case (all actual positives are predicted positive) gives 1.0 under that definition, matching the reference code.

```python
def test_recall_3(self):
    mc = MetricsCalculator()
    temp = mc.recall([1, 1, 0, 1], [1, 0, 0, 1])
    self.assertEqual(temp, 1.0)
```

**test_recall_4**: `stated`
- reason: The docstring defines recall as the standard TP/(TP+FN) with label 1 as positive, and the test's inputs give 2 true positives and 1 false negative, so a programmer following it would return 2/3.

```python
def test_recall_4(self):
    mc = MetricsCalculator()
    temp = mc.recall([1, 1, 0, 0], [1, 1, 0, 1])
    self.assertAlmostEqual(temp, 0.6666666666666666)
```

**test_recall_5**: `stated`
- reason: The docstring defines recall as the fraction of true positives among actual positives, and this test's inputs give one true positive and two false negatives, so a programmer following it would return 1/3.

```python
def test_recall_5(self):
    mc = MetricsCalculator()
    temp = mc.recall([1, 1, 0, 0], [1, 0, 1, 1])
    self.assertAlmostEqual(temp, 0.3333333333333333)
```

**test_recall_6**: `unstated`
- reason: The docstring defines recall as true positives over actual positives but says nothing about the case with no actual positives, where a programmer could raise ZeroDivisionError or return NaN instead of the 0.0 the test expects.
- missing: The docstring should state that when there are no actual positive labels in true_labels (so the denominator is zero), recall returns 0.0.

```python
def test_recall_6(self):
    mc = MetricsCalculator()
    temp = mc.recall([1, 1, 0, 0], [0, 0, 0, 0])
    self.assertEqual(temp, 0.0)
```

## Method `f1_score`

### Docstring

```python
def f1_score(self, predicted_labels, true_labels):
        """
        Calculate f1 score, which is the harmonic mean of precision and recall
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>> mc.f1_score([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
```

### Reference code (`solution_code`)

```python
def f1_score(self, predicted_labels, true_labels):
        self.update(predicted_labels, true_labels)
        precision = self.precision(predicted_labels, true_labels)
        recall = self.recall(predicted_labels, true_labels)
        if precision + recall == 0.0:
            return 0.0
        return (2 * precision * recall) / (precision + recall)
```

### Tests (`MetricsCalculatorTestF1Score`)

**test_f1_score_1**: `stated`
- reason: The docstring's own example uses the same inputs and expected value (0.5) as this test, and a programmer computing the harmonic mean of precision and recall would get that result.

```python
def test_f1_score_1(self):
    mc = MetricsCalculator()
    temp = mc.f1_score([1, 1, 0, 0], [1, 0, 0, 1])
    self.assertEqual(temp, 0.5)
```

**test_f1_score_2**: `unstated`
- reason: The docstring defines F1 as the harmonic mean of precision and recall but never says which label counts as positive, and the test's expected 0.4 depends on treating label 1 as the positive class, which a programmer could not infer from the symmetric example.
- missing: The docstring should state which label is treated as the positive class for precision and recall (or whether scores are averaged across classes) so that an implementation with a different convention does not produce a different value.

```python
def test_f1_score_2(self):
    mc = MetricsCalculator()
    temp = mc.f1_score([1, 1, 1, 0], [1, 0, 0, 1])
    self.assertEqual(temp, 0.4)
```

**test_f1_score_3**: `stated`
- reason: The docstring defines f1 as the harmonic mean of precision and recall, and the standard definitions (positive class 1, precision = TP/(TP+FP), recall = TP/(TP+FN)) give 2/3 and 1, so the expected 0.8 follows.

```python
def test_f1_score_3(self):
    mc = MetricsCalculator()
    temp = mc.f1_score([1, 1, 0, 1], [1, 0, 0, 1])
    self.assertEqual(temp, 0.8)
```

**test_f1_score_4**: `unstated`
- reason: The docstring says F1 is the harmonic mean of precision and recall but never says which label counts as positive or whether scores are averaged across classes, and the test's expected 0.8 depends on that choice (the example's 0.5 fits both conventions).
- missing: The docstring should state which label is treated as the positive class (and how precision and recall are aggregated when there are multiple label values), with a worked example where the choices give different results.

```python
def test_f1_score_4(self):
    mc = MetricsCalculator()
    temp = mc.f1_score([1, 1, 0, 0], [1, 1, 0, 1])
    self.assertEqual(temp, 0.8)
```

**test_f1_score_5**: `stated`
- reason: The docstring defines F1 as the harmonic mean of precision and recall, and the standard binary definitions with label 1 as positive give 0.4 for this input, matching the test.

```python
def test_f1_score_5(self):
    mc = MetricsCalculator()
    temp = mc.f1_score([1, 1, 0, 0], [1, 0, 1, 1])
    self.assertEqual(temp, 0.4)
```

**test_f1_score_6**: `unstated`
- reason: The docstring defines F1 as the harmonic mean of precision and recall but does not say what to return when both are undefined or zero, as with all-negative labels, so a correct implementation could return NaN or 1.0 and fail the test's expected 0.0.
- missing: The docstring should state the return value when precision and recall have zero denominators (no predicted positives or no true positives), for example that F1 is 0.0 whenever precision plus recall is zero.

```python
def test_f1_score_6(self):
    mc = MetricsCalculator()
    temp = mc.f1_score([0, 0, 0, 0], [0, 0, 0, 0])
    self.assertEqual(temp, 0.0)
```

## Method `accuracy`

### Docstring

```python
def accuracy(self, predicted_labels, true_labels):
        """
        Calculate accuracy
        :param predicted_labels: list, predicted results
        :param true_labels: list, true labels
        :return: float
        >>> mc = MetricsCalculator()
        >>>mc.accuracy([1, 1, 0, 0], [1, 0, 0, 1])
        0.5
        """
```

### Reference code (`solution_code`)

```python
def accuracy(self, predicted_labels, true_labels):
        self.update(predicted_labels, true_labels)
        total = self.true_positives + self.true_negatives + self.false_positives + self.false_negatives
        if total == 0:
            return 0.0
        return (self.true_positives + self.true_negatives) / total
```

### Tests (`MetricsCalculatorTestAccuracy`)

**test_accuracy_1**: `stated`
- reason: The docstring example `accuracy([1, 1, 0, 0], [1, 0, 0, 1])` returns 0.5, and a programmer computing the fraction of matching positions would get 2/4 = 0.5, which is exactly what the test expects.

```python
def test_accuracy_1(self):
    mc = MetricsCalculator()
    temp = mc.accuracy([1, 1, 0, 0], [1, 0, 0, 1])
    self.assertEqual(temp, 0.5)
```

**test_accuracy_2**: `unstated`
- reason: The docstring never says how a predicted label that is neither 0 nor 1 is handled, but the test expects such pairs to be ignored, so a programmer could reasonably count them as errors or raise an exception instead.
- missing: The docstring should state that pairs whose predicted or true label is not one of the expected binary values are excluded from both the numerator and the denominator, so the accuracy is computed only over the valid pairs.

```python
def test_accuracy_2(self):
    mc = MetricsCalculator()
    temp = mc.accuracy([1, 1, 2, 0], [1, 0, 0, 1])
    self.assertAlmostEqual(temp, 0.3333333333333333)
```

**test_accuracy_3**: `stated`
- reason: Accuracy is the standard fraction of matching predictions, and the docstring's example confirms it, so a programmer would compute 3 correct out of 4 as 0.75 and pass the test.

```python
def test_accuracy_3(self):
    mc = MetricsCalculator()
    temp = mc.accuracy([1, 1, 0, 1], [1, 0, 0, 1])
    self.assertEqual(temp, 0.75)
```

**test_accuracy_4**: `stated`
- reason: The docstring's example (2 of 4 matching gives 0.5) defines accuracy as the fraction of positions where predictions match the true labels, so a programmer would compute 3/4 = 0.75 for this test.

```python
def test_accuracy_4(self):
    mc = MetricsCalculator()
    temp = mc.accuracy([1, 1, 0, 0], [1, 1, 0, 1])
    self.assertEqual(temp, 0.75)
```

**test_accuracy_5**: `stated`
- reason: The docstring defines accuracy as the fraction of predictions that match the true labels, and the test's inputs give 1 correct out of 4 (0.25), which a programmer following that definition would produce.

```python
def test_accuracy_5(self):
    mc = MetricsCalculator()
    temp = mc.accuracy([1, 1, 0, 0], [1, 0, 1, 1])
    self.assertEqual(temp, 0.25)
```

**test_accuracy_6**: `unstated`
- reason: The docstring gives no behaviour for empty inputs, so a programmer computing correct predictions divided by the number of samples would hit a division by zero, while the test expects 0.0.
- missing: The docstring should state what the function returns when the input lists are empty (for example, 0.0 instead of raising a division-by-zero error).

```python
def test_accuracy_6(self):
    mc = MetricsCalculator()
    temp = mc.accuracy([], [])
    self.assertEqual(temp, 0.0)
```

## Tests in no method's test class

### `MetricsCalculatorTest`

**test_metricscalculator**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_metricscalculator(self):
    mc = MetricsCalculator()
    self.assertEqual((mc.true_positives, mc.false_positives, mc.false_negatives, mc.true_negatives), (0, 0, 0, 0))
    mc.update([1, 1, 0, 0], [1, 0, 0, 1])
    self.assertEqual((mc.true_positives, mc.false_positives, mc.false_negatives, mc.true_negatives), (1, 1, 1, 1))
    temp = mc.precision([1, 1, 0, 0], [1, 0, 0, 1])
    self.assertEqual(temp, 0.5)
    temp = mc.recall([1, 1, 0, 0], [1, 0, 0, 1])
    self.assertEqual(temp, 0.5)
    temp = mc.f1_score([1, 1, 0, 0], [1, 0, 0, 1])
    self.assertEqual(temp, 0.5)
    temp = mc.accuracy([1, 1, 0, 0], [1, 0, 0, 1])
    self.assertEqual(temp, 0.5)
```
