# ClassEval_57

## Skeleton (what the agent sees)

```python
import numpy as np


class MetricsCalculator2:
    """
    The class provides to calculate Mean Reciprocal Rank (MRR) and Mean Average Precision (MAP) based on input data, where MRR measures the ranking quality and MAP measures the average precision.
    """

    def __init__(self):
        pass

    @staticmethod
    def mrr(data):
        """
        compute the MRR of the input data. MRR is a widely used evaluation index. It is the mean of reciprocal rank.
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
         ([1,0,...],5),
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        >>> MetricsCalculator2.mrr(([1, 0, 1, 0], 4))
        >>> MetricsCalculator2.mrr([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        1.0, [1.0]
        0.75, [1.0, 0.5]
        """


    @staticmethod
    def map(data):
        """
        compute the MAP of the input data. MAP is a widely used evaluation index. It is the mean of AP (average precision).
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
         ([1,0,...],5),
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        >>> MetricsCalculator2.map(([1, 0, 1, 0], 4))
        >>> MetricsCalculator2.map([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        0.41666666666666663, [0.41666666666666663]
        0.3333333333333333, [0.41666666666666663, 0.25]
        """
```

## Method `mrr`

### Docstring

```python
def mrr(data):
        """
        compute the MRR of the input data. MRR is a widely used evaluation index. It is the mean of reciprocal rank.
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
         ([1,0,...],5),
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        >>> MetricsCalculator2.mrr(([1, 0, 1, 0], 4))
        >>> MetricsCalculator2.mrr([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        1.0, [1.0]
        0.75, [1.0, 0.5]
        """
```

### Reference code (`solution_code`)

```python
def mrr(data):
        if type(data) != list and type(data) != tuple:
            raise Exception("the input must be a tuple([0,...,1,...],int) or a iteration of list of tuple")

        if len(data) == 0:
            return 0.0, [0.0]
        if type(data) == tuple:
            (sub_list, total_num) = data
            sub_list = np.array(sub_list)
            if total_num == 0:
                return 0.0, [0.0]
            else:
                ranking_array = 1.0 / (np.array(list(range(len(sub_list)))) + 1)
                mr_np = sub_list * ranking_array

                mr = 0.0
                for team in mr_np:
                    if team > 0:
                        mr = team
                        break
                return mr, [mr]

        if type(data) == list:
            separate_result = []
            for (sub_list, total_num) in data:
                sub_list = np.array(sub_list)

                if total_num == 0:
                    mr = 0.0
                else:
                    ranking_array = 1.0 / (np.array(list(range(len(sub_list)))) + 1)
                    mr_np = sub_list * ranking_array

                    mr = 0.0
                    for team in mr_np:
                        if team > 0:
                            mr = team
                            break

                separate_result.append(mr)
            return np.mean(separate_result), separate_result
```

### Tests (`MetricsCalculator2TestMrr`)

**test_mrr_1**: `stated`
- reason: The docstring's example outputs "1.0, [1.0]" for a single `([1, 0, 1, 0], 4)` tuple, and a programmer applying "mean of reciprocal rank" (first correct answer at rank 1 gives 1.0) with the second return as a per-input list would produce exactly the tested result.

```python
def test_mrr_1(self):
    mc2 = MetricsCalculator2()
    res1, res2 = MetricsCalculator2.mrr(([1, 0, 1, 0], 4))
    self.assertEqual(res1, 1.0)
    self.assertEqual(res2, [1.0])
```

**test_mrr_2**: `stated`
- reason: The docstring defines MRR as the mean of reciprocal ranks, and its list example (1.0 and 0.5 averaging to 0.75) shows the rank is the position of the first correct answer, so a programmer would produce 1/4 = 0.25 for this single tuple.

```python
def test_mrr_2(self):
    res1, res2 = MetricsCalculator2.mrr(([0, 0, 0, 1], 4))
    self.assertEqual(res1, 0.25)
    self.assertEqual(res2, [0.25])
```

**test_mrr_3**: `stated`
- reason: The docstring's example `0.75, [1.0, 0.5]` for the list input `[([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)]` matches the test exactly, and a reciprocal-rank implementation gives 1.0 and 0.5 per entry, averaging to 0.75.

```python
def test_mrr_3(self):
    res1, res2 = MetricsCalculator2.mrr([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
    self.assertEqual(res1, 0.75)
    self.assertEqual(res2, [1.0, 0.5])
```

**test_mrr_4**: `stated`
- reason: The docstring defines MRR as the mean of reciprocal rank and its example (`[0,1,0,1]` giving 0.5 and the mean 0.75) shows the reciprocal of the position of the first correct answer, so a programmer would compute 1/4 for a first hit at rank 4 and get 0.625 overall.

```python
def test_mrr_4(self):
    res1, res2 = MetricsCalculator2.mrr([([1, 1, 1, 0], 4), ([0, 0, 0, 1], 4)])
    self.assertEqual(res1, 0.625)
    self.assertEqual(res2, [1.0, 0.25])
```

**test_mrr_5**: `stated`
- reason: The docstring says MRR is the mean of reciprocal rank, returns the average over the list plus a per-input list, and its example for a two-tuple list gives 0.75 and [1.0, 0.5], which is the behaviour this test checks.

```python
def test_mrr_5(self):
    res1, res2 = MetricsCalculator2.mrr([([1, 0, 1, 1], 4), ([0, 1, 0, 0], 4)])
    self.assertEqual(res1, 0.75)
    self.assertEqual(res2, [1.0, 0.5])
```

**test_mrr_6**: `stated`
- reason: The test calls `mrr(1)` inside a try/except that swallows every exception and makes no assertion, so any implementation passes it and a programmer following the docstring will pass.

```python
def test_mrr_6(self):
    try:
        MetricsCalculator2.mrr(1)
    except:
        pass
```

**test_mrr_7**: `unstated`
- reason: The docstring never says what happens for an empty input list, so a programmer could reasonably raise an error or return NaN from the mean, and the test expects (0.0, [0.0]).
- missing: The docstring should state that when the input contains no entries, the function returns a score of 0.0 together with a per-item list containing a single 0.0, rather than raising an error or returning NaN.

```python
def test_mrr_7(self):
    res1, res2 = MetricsCalculator2.mrr([])
    self.assertEqual(res1, 0.0)
    self.assertEqual(res2, [0.0])
```

**test_mrr_8**: `unstated`
- reason: The docstring never says what an item with a ground-truth total of zero should score, so a programmer computing reciprocal rank from the results would return 1.0 for the first item here, while the test expects 0.0.
- missing: When an input's ground-truth total is zero, its reciprocal rank is 0.0 regardless of its 0/1 results, and that 0.0 still counts toward the mean and appears in the per-item list.

```python
def test_mrr_8(self):
    res1, res2 = MetricsCalculator2.mrr([([1, 0, 1, 1], 0), ([0, 1, 0, 0], 0)])
    self.assertEqual(res1, 0.0)
    self.assertEqual(res2, [0.0, 0.0])
```

## Method `map`

### Docstring

```python
@staticmethod
    def map(data):
        """
        compute the MAP of the input data. MAP is a widely used evaluation index. It is the mean of AP (average precision).
        :param data: the data must be a tuple, list 0,1,eg.([1,0,...],5).  In each tuple (actual result,ground truth num),ground truth num is the total ground num.
         ([1,0,...],5),
        or list of tuple eg. [([1,0,1,...],5),([1,0,...],6),([0,0,...],5)].
        1 stands for a correct answer, 0 stands for a wrong answer.
        :return: if input data is list, return the recall of this list. if the input data is list of list, return the
        average recall on all list. The second return value is a list of precision for each input.
        >>> MetricsCalculator2.map(([1, 0, 1, 0], 4))
        >>> MetricsCalculator2.map([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
        0.41666666666666663, [0.41666666666666663]
        0.3333333333333333, [0.41666666666666663, 0.25]
        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def map(data):
        if type(data) != list and type(data) != tuple:
            raise Exception("the input must be a tuple([0,...,1,...],int) or a iteration of list of tuple")

        if len(data) == 0:
            return 0.0, [0.0]
        if type(data) == tuple:
            (sub_list, total_num) = data
            sub_list = np.array(sub_list)
            if total_num == 0:
                return 0.0, [0.0]
            else:
                ranking_array = 1.0 / (np.array(list(range(len(sub_list)))) + 1)

                right_ranking_list = []
                count = 1
                for t in sub_list:
                    if t == 0:
                        right_ranking_list.append(0)
                    else:
                        right_ranking_list.append(count)
                        count += 1

                ap = np.sum(np.array(right_ranking_list) * ranking_array) / total_num
                return ap, [ap]

        if type(data) == list:
            separate_result = []
            for (sub_list, total_num) in data:
                sub_list = np.array(sub_list)

                if total_num == 0:
                    ap = 0.0
                else:
                    ranking_array = 1.0 / (np.array(list(range(len(sub_list)))) + 1)

                    right_ranking_list = []
                    count = 1
                    for t in sub_list:
                        if t == 0:
                            right_ranking_list.append(0)
                        else:
                            right_ranking_list.append(count)
                            count += 1

                    ap = np.sum(np.array(right_ranking_list) * ranking_array) / total_num

                separate_result.append(ap)
            return np.mean(separate_result), separate_result
```

### Tests (`MetricsCalculator2TestMap`)

**test_map_1**: `stated`
- reason: The docstring's first example shows that a single (flags, total) tuple returns the AP value 0.41666... together with the one-element list [0.41666...], which is exactly what this test checks.

```python
def test_map_1(self):
    res1, res2 = MetricsCalculator2.map(([1, 0, 1, 0], 4))
    self.assertEqual(res1, 0.41666666666666663)
    self.assertEqual(res2, [0.41666666666666663])
```

**test_map_2**: `stated`
- reason: The docstring's examples (e.g. `([1, 0, 1, 0], 4)` giving 0.41666) show that AP sums the precision at each correct position and divides by the total ground-truth count, which gives 0.0625 for `([0, 0, 0, 1], 4)`.

```python
def test_map_2(self):
    res1, res2 = MetricsCalculator2.map(([0, 0, 0, 1], 4))
    self.assertEqual(res1, 0.0625)
    self.assertEqual(res2, [0.0625])
```

**test_map_3**: `stated`
- reason: The docstring's second example gives the exact output this test checks, a mean of 0.3333333333333333 and per-input list [0.41666666666666663, 0.25] for the list-of-tuples input.

```python
def test_map_3(self):
    res1, res2 = MetricsCalculator2.map([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
    self.assertEqual(res1, 0.3333333333333333)
    self.assertEqual(res2, [0.41666666666666663, 0.25])
```

**test_map_4**: `unstated`
- reason: The test expects the mean of per-sequence AP values (each sum of hit-position precisions divided by the total ground-truth count), and the docstring never states that formula, so a programmer could easily get 0.40625 wrong.
- missing: The docstring should state the exact AP formula: for each item, add the precision (correct hits so far divided by position) at every position holding a 1, then divide by the stated total ground-truth count, and the MAP is the mean of those per-item values.

```python
def test_map_4(self):
    res1, res2 = MetricsCalculator2.map([([1, 1, 1, 0], 4), ([0, 0, 0, 1], 4)])
    self.assertEqual(res1, 0.40625)
    self.assertEqual(res2, [0.75, 0.0625])
```

**test_map_5**: `stated`
- reason: The docstring's examples for a list of (ranking, ground-truth count) tuples show the AP computation (precision at each correct position divided by the ground-truth count) and the mean across the list, which is exactly what this test checks.

```python
def test_map_5(self):
    res1, res2 = MetricsCalculator2.map([([1, 0, 1, 1], 4), ([0, 1, 0, 0], 4)])
    self.assertEqual(res1, 0.3645833333333333)
    self.assertEqual(res2, [0.6041666666666666, 0.125])
```

**test_map_6**: `stated`
- reason: The test passes an int, which the docstring's requirement that input be a tuple or list excludes, and its bare try/except accepts any outcome, so an implementation following the docstring passes.

```python
def test_map_6(self):
    try:
        MetricsCalculator2.map(1)
    except:
        pass
```

**test_map_7**: `unstated`
- reason: The docstring never says what an empty input list should return, so a correct implementation might raise an error or return NaN from averaging an empty list instead of the expected 0.0 and [0.0].
- missing: The docstring should specify the return value when the input collection has no entries, including the scalar average and the per-item list each should be.

```python
def test_map_7(self):
    res1, res2 = MetricsCalculator2.map([])
    self.assertEqual(res1, 0.0)
    self.assertEqual(res2, [0.0])
```

**test_map_8**: `unstated`
- reason: The docstring never says what AP a (results, ground-truth count) entry should get when its ground-truth count is zero, so a programmer computing precision over the relevant hits would divide by zero or produce a different value than the test's expected 0.0 per entry.
- missing: The docstring should state that any entry whose ground-truth total is zero contributes an AP of 0.0 to the per-input list and to the mean, regardless of its result values.

```python
def test_map_8(self):
    res1, res2 = MetricsCalculator2.map([([1, 0, 1, 1], 0), ([0, 1, 0, 0], 0)])
    self.assertEqual(res1, 0.0)
    self.assertEqual(res2, [0.0, 0.0])
```

## Tests in no method's test class

### `MetricsCalculator2Test`

**test_metricscalculator2_1**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_metricscalculator2_1(self):
    res1, res2 = MetricsCalculator2.mrr(([1, 0, 1, 0], 4))
    self.assertEqual(res1, 1.0)
    self.assertEqual(res2, [1.0])
```

**test_metricscalculator2_2**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_metricscalculator2_2(self):
    res1, res2 = MetricsCalculator2.mrr([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
    self.assertEqual(res1, 0.75)
    self.assertEqual(res2, [1.0, 0.5])
```

**test_metricscalculator2_3**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_metricscalculator2_3(self):
    res1, res2 = MetricsCalculator2.map(([1, 0, 1, 0], 4))
    self.assertEqual(res1, 0.41666666666666663)
    self.assertEqual(res2, [0.41666666666666663])
```

**test_metricscalculator2_4**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_metricscalculator2_4(self):
    res1, res2 = MetricsCalculator2.map([([1, 0, 1, 0], 4), ([0, 1, 0, 1], 4)])
    self.assertEqual(res1, 0.3333333333333333)
    self.assertEqual(res2, [0.41666666666666663, 0.25])
```
