# ClassEval_93

## Skeleton (what the agent sees)

```python
import numpy as np
from gensim import matutils
from numpy import dot, array

class VectorUtil:
    """
    The class provides vector operations, including calculating similarity, cosine similarities, average similarity, and IDF weights.
    """

    @staticmethod
    def similarity(vector_1, vector_2):
        """
        Compute the cosine similarity between one vector and another vector.
        :param vector_1: numpy.ndarray, Vector from which similarities are to be computed, expected shape (dim,).
        :param vector_2: numpy.ndarray, Vector from which similarities are to be computed, expected shape (dim,).
        :return: numpy.ndarray, Contains cosine distance between `vector_1` and `vector_2`
        >>> vector_1 = np.array([1, 1])
        >>> vector_2 = np.array([1, 0])
        >>> VectorUtil.similarity(vector_1, vector_2)
        0.7071067811865475
        """


    @staticmethod
    def cosine_similarities(vector_1, vectors_all):
        """
        Compute cosine similarities between one vector and a set of other vectors.
        :param vector_1: numpy.ndarray, Vector from which similarities are to be computed, expected shape (dim,).
        :param vectors_all: list of numpy.ndarray, For each row in vectors_all, distance from vector_1 is computed, expected shape (num_vectors, dim).
        :return: numpy.ndarray, Contains cosine distance between `vector_1` and each row in `vectors_all`, shape (num_vectors,).
        >>> vector1 = np.array([1, 2, 3])
        >>> vectors_all = [np.array([4, 5, 6]), np.array([7, 8, 9])]
        >>> VectorUtil.cosine_similarities(vector1, vectors_all)
        [0.97463185 0.95941195]
        """


    @staticmethod
    def n_similarity(vector_list_1, vector_list_2):
        """
        Compute cosine similarity between two sets of vectors.
        :param vector_list_1: list of numpy vector
        :param vector_list_2: list of numpy vector
        :return: numpy.ndarray, Similarities between vector_list_1 and vector_list_2.
        >>> vector_list1 = [np.array([1, 2, 3]), np.array([4, 5, 6])]
        >>> vector_list2 = [np.array([7, 8, 9]), np.array([10, 11, 12])]
        >>> VectorUtil.n_similarity(vector_list1, vector_list2)
        0.9897287473881233
        """


    @staticmethod
    def compute_idf_weight_dict(total_num, number_dict):
        """
        Calculate log(total_num+1/count+1) for each count in number_dict
        :param total_num: int
        :param number_dict: dict
        :return: dict
        >>> num_dict = {'key1':0.1, 'key2':0.5}
        >>> VectorUtil.compute_idf_weight_dict(2, num_dict)
        {'key1': 1.0033021088637848, 'key2': 0.6931471805599453}
        """
```

## Method `similarity`

### Docstring

```python
def similarity(vector_1, vector_2):
        """
        Compute the cosine similarity between one vector and another vector.
        :param vector_1: numpy.ndarray, Vector from which similarities are to be computed, expected shape (dim,).
        :param vector_2: numpy.ndarray, Vector from which similarities are to be computed, expected shape (dim,).
        :return: numpy.ndarray, Contains cosine distance between `vector_1` and `vector_2`
        >>> vector_1 = np.array([1, 1])
        >>> vector_2 = np.array([1, 0])
        >>> VectorUtil.similarity(vector_1, vector_2)
        0.7071067811865475
        """
```

### Reference code (`solution_code`)

```python
def similarity(vector_1, vector_2):
        return dot(matutils.unitvec(vector_1), matutils.unitvec(vector_2))
```

### Tests (`VectorUtilTestSimilarity`)

**test_similarity_1**: `stated`
- reason: The docstring defines the method as cosine similarity and its example gives 0.7071067811865475 for [1,1] and [1,0], which is exactly what the test checks.

```python
def test_similarity_1(self):
    vector_1 = np.array([1, 1])
    vector_2 = np.array([1, 0])
    similarity = VectorUtil.similarity(vector_1, vector_2)
    self.assertAlmostEqual(similarity, 0.7071067811865475)
```

**test_similarity_2**: `unstated`
- reason: The test expects a similarity of 0.0 when one input is the zero vector, but the docstring only describes cosine similarity, which a programmer would compute as a division by zero (NaN or an error) for that case.
- missing: The docstring should specify what is returned when either input vector has zero norm, such as 0.0 instead of dividing by zero.

```python
def test_similarity_2(self):
    vector_1 = np.array([1, 1])
    vector_2 = np.array([0, 0])
    similarity = VectorUtil.similarity(vector_1, vector_2)
    self.assertAlmostEqual(similarity, 0.0)
```

**test_similarity_3**: `stated`
- reason: The docstring defines the output as cosine similarity, and the cosine similarity of a vector with itself is 1.0, so a programmer following it would pass this test.

```python
def test_similarity_3(self):
    vector_1 = np.array([1, 1])
    vector_2 = np.array([1, 1])
    similarity = VectorUtil.similarity(vector_1, vector_2)
    self.assertAlmostEqual(similarity, 1.0)
```

**test_similarity_4**: `stated`
- reason: The docstring defines the method as cosine similarity, and a standard cosine computation on this test's vectors gives 4/(2·√5) ≈ 0.8944, matching the expected value.

```python
def test_similarity_4(self):
    vector_1 = np.array([1, 1, 0, 1, 0, 1, 0, 1])
    vector_2 = np.array([1, 0, 0, 1, 0, 1, 0, 1])
    similarity = VectorUtil.similarity(vector_1, vector_2)
    self.assertAlmostEqual(similarity, 0.8944271909999159)
```

**test_similarity_5**: `unstated`
- reason: The test passes a zero vector and expects a similarity of 0.0, but the docstring only gives the cosine formula, which is undefined when a norm is zero, so a programmer would likely divide by zero and return NaN.
- missing: The docstring should say that if either input vector has zero norm, the function returns 0 instead of dividing by zero.

```python
def test_similarity_5(self):
    vector_1 = np.array([1, 1, 1, 1, 1, 1, 1, 1])
    vector_2 = np.array([0, 0, 0, 0, 0, 0, 0, 0])
    similarity = VectorUtil.similarity(vector_1, vector_2)
    self.assertAlmostEqual(similarity, 0.0)
```

## Method `cosine_similarities`

### Docstring

```python
@staticmethod
    def cosine_similarities(vector_1, vectors_all):
        """
        Compute cosine similarities between one vector and a set of other vectors.
        :param vector_1: numpy.ndarray, Vector from which similarities are to be computed, expected shape (dim,).
        :param vectors_all: list of numpy.ndarray, For each row in vectors_all, distance from vector_1 is computed, expected shape (num_vectors, dim).
        :return: numpy.ndarray, Contains cosine distance between `vector_1` and each row in `vectors_all`, shape (num_vectors,).
        >>> vector1 = np.array([1, 2, 3])
        >>> vectors_all = [np.array([4, 5, 6]), np.array([7, 8, 9])]
        >>> VectorUtil.cosine_similarities(vector1, vectors_all)
        [0.97463185 0.95941195]
        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def cosine_similarities(vector_1, vectors_all):
        norm = np.linalg.norm(vector_1)
        all_norms = np.linalg.norm(vectors_all, axis=1)
        dot_products = dot(vectors_all, vector_1)
        similarities = dot_products / (norm * all_norms)
        return similarities
```

### Tests (`VectorUtilTestCosineSimilarities`)

**test_cosine_similarities_1**: `stated`
- reason: The docstring's example output (about 0.975 for [1,2,3] vs [4,5,6]) is the cosine similarity value, which is what this test checks for [1,1] vs [1,0] and [1,1], even though the return description wrongly says "cosine distance".

```python
def test_cosine_similarities_1(self):
    vector1 = np.array([1, 1])
    vectors_all = [np.array([1, 0]), np.array([1, 1])]
    similarities = VectorUtil.cosine_similarities(vector1, vectors_all)
    res = [0.7071067811865475, 1.0]
    for index, item in enumerate(similarities):
        self.assertAlmostEqual(item, res[index])
```

**test_cosine_similarities_2**: `stated`
- reason: The docstring asks for cosine similarity between one vector and each row of a matrix, and its example values match the standard formula, which is what the test checks on binary vectors.

```python
def test_cosine_similarities_2(self):
    vector1 = np.array([1, 1, 0, 0, 1, 0, 1, 0])
    vectors_all = [np.array([1, 0, 0, 0, 1, 0, 1, 0]), np.array([1, 1, 0, 1, 1, 1, 1, 0])]
    similarities = VectorUtil.cosine_similarities(vector1, vectors_all)
    res = [0.8660254037844387, 0.8164965809277261]
    for index, item in enumerate(similarities):
        self.assertAlmostEqual(item, res[index])
```

**test_cosine_similarities_3**: `contradicts`
- reason: The docstring's first line and example describe cosine similarity, but the return description says "cosine distance", which conflicts with the test's expected values (e.g. 3/(2·√3) ≈ 0.866), which are similarities.
- missing: The docstring should state that each output is the cosine similarity (dot product divided by the product of the two vector norms, ranging from -1 to 1), not a distance such as 1 minus similarity.

```python
def test_cosine_similarities_3(self):
    vector1 = np.array([1, 1, 0, 0, 1, 0, 1, 0])
    vectors_all = [np.array([1, 0, 0, 0, 1, 0, 1, 0]), np.array([1, 1, 1, 1, 1, 1, 1, 0])]
    similarities = VectorUtil.cosine_similarities(vector1, vectors_all)
    res = [0.8660254037844387, 0.7559289460184544]
    for index, item in enumerate(similarities):
        self.assertAlmostEqual(item, res[index])
```

**test_cosine_similarities_4**: `stated`
- reason: The summary and the example output both describe cosine similarity, which is what the reference code computes and what this test checks, so a programmer following the docstring would get the expected values.

```python
def test_cosine_similarities_4(self):
    vector1 = np.array([1, 1, 0, 0, 1, 0, 1, 0])
    vectors_all = [np.array([1, 0, 0, 0, 1, 0, 1, 0]), np.array([1, 1, 1, 1, 1, 1, 1, 1])]
    similarities = VectorUtil.cosine_similarities(vector1, vectors_all)
    res = [0.8660254037844387, 0.7071067811865475]
    for index, item in enumerate(similarities):
        self.assertAlmostEqual(item, res[index])
```

**test_cosine_similarities_5**: `contradicts`
- reason: The docstring's return description says "cosine distance", but the test expects cosine similarity values (dot product divided by the product of norms, e.g. 0.866 for the first pair), which is what the reference code computes.
- missing: The return description should say the function returns the cosine similarity (dot product divided by the product of the two vector norms, ranging from -1 to 1), not a distance such as one minus similarity.

```python
def test_cosine_similarities_5(self):
    vector1 = np.array([1, 1, 0, 0, 1, 0, 1, 0])
    vectors_all = [np.array([1, 0, 0, 0, 1, 0, 1, 0]), np.array([0, 1, 1, 1, 1, 1, 1, 1])]
    similarities = VectorUtil.cosine_similarities(vector1, vectors_all)
    res = [0.8660254037844387, 0.5669467095138409]
    for index, item in enumerate(similarities):
        self.assertAlmostEqual(item, res[index])
```

## Method `n_similarity`

### Docstring

```python
@staticmethod
    def n_similarity(vector_list_1, vector_list_2):
        """
        Compute cosine similarity between two sets of vectors.
        :param vector_list_1: list of numpy vector
        :param vector_list_2: list of numpy vector
        :return: numpy.ndarray, Similarities between vector_list_1 and vector_list_2.
        >>> vector_list1 = [np.array([1, 2, 3]), np.array([4, 5, 6])]
        >>> vector_list2 = [np.array([7, 8, 9]), np.array([10, 11, 12])]
        >>> VectorUtil.n_similarity(vector_list1, vector_list2)
        0.9897287473881233
        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def n_similarity(vector_list_1, vector_list_2):
        if not (len(vector_list_1) and len(vector_list_2)):
            raise ZeroDivisionError('At least one of the passed list is empty.')

        return dot(matutils.unitvec(array(vector_list_1).mean(axis=0)),
                   matutils.unitvec(array(vector_list_2).mean(axis=0)))
```

### Tests (`VectorUtilTestNSimilarity`)

**test_n_similarity_1**: `unstated`
- reason: The docstring says "cosine similarity between two sets of vectors" without saying each list is first averaged into one mean vector, so a programmer could compute pairwise or other aggregate similarities and fail this test's expected 1.0.
- missing: The docstring should state that each list's vectors are averaged element-wise into a single mean vector, and the cosine similarity is computed between those two mean vectors.

```python
def test_n_similarity_1(self):
    vector_list1 = [np.array([1, 0]), np.array([0, 1])]
    vector_list2 = [np.array([0, 0]), np.array([1, 1])]
    similarity = VectorUtil.n_similarity(vector_list1, vector_list2)
    self.assertAlmostEqual(similarity, 1.0)
```

**test_n_similarity_2**: `unstated`
- reason: The docstring only says "cosine similarity between two sets of vectors," so a programmer could average pairwise cosines or use another aggregation, which would not give the value the test expects.
- missing: The docstring should state that each list is first reduced to a single vector by element-wise mean, and the result is the cosine similarity between those two mean vectors.

```python
def test_n_similarity_2(self):
    vector_list1 = [np.array([1, 1]), np.array([0, 1])]
    vector_list2 = [np.array([0, 0]), np.array([1, 1])]
    similarity = VectorUtil.n_similarity(vector_list1, vector_list2)
    self.assertAlmostEqual(similarity, 0.9486832980505137)
```

**test_n_similarity_3**: `unstated`
- reason: The test expects the cosine of the element-wise means of the two lists, which the docstring never states; it only gives one example whose value happens to match that rule, so a programmer could reasonably average pairwise similarities instead.
- missing: The docstring should say that each list is first reduced to its element-wise mean vector, and the cosine similarity is then computed between those two mean vectors, rather than averaging pairwise similarities.

```python
def test_n_similarity_3(self):
    vector_list1 = [np.array([1, 0]), np.array([1, 1])]
    vector_list2 = [np.array([0, 0]), np.array([1, 1])]
    similarity = VectorUtil.n_similarity(vector_list1, vector_list2)
    self.assertAlmostEqual(similarity, 0.9486832980505137)
```

**test_n_similarity_4**: `unstated`
- reason: The docstring says only "cosine similarity between two sets of vectors" and does not say the sets are reduced to mean vectors before the cosine is taken, so a programmer could reasonably average pairwise cosines and fail this test's expected 0.9487.
- missing: The docstring should state how each list is reduced to a single vector before comparison (for example, the element-wise mean of the vectors in each list, then the cosine of those two means).

```python
def test_n_similarity_4(self):
    vector_list1 = [np.array([1, 0]), np.array([0, 1])]
    vector_list2 = [np.array([1, 0]), np.array([1, 1])]
    similarity = VectorUtil.n_similarity(vector_list1, vector_list2)
    self.assertAlmostEqual(similarity, 0.9486832980505137)
```

**test_n_similarity_5**: `unstated`
- reason: The docstring only says "cosine similarity between two sets of vectors" without saying how a set is reduced to one vector, so a programmer could plausibly average pairwise cosine similarities instead of taking the cosine of the element-wise means that this test expects.
- missing: The docstring should state that each list is first collapsed to the element-wise mean vector, and the result is the cosine similarity between those two mean vectors.

```python
def test_n_similarity_5(self):
    vector_list1 = [np.array([1, 0]), np.array([0, 1])]
    vector_list2 = [np.array([0, 1]), np.array([1, 1])]
    similarity = VectorUtil.n_similarity(vector_list1, vector_list2)
    self.assertAlmostEqual(similarity, 0.9486832980505137)
```

**test_n_similarity_6**: `stated`
- reason: The test wraps the empty-list call in a bare try/except with no assertion, so any implementation passes whether it raises or returns a value.

```python
def test_n_similarity_6(self):
    try:
        vector_list1 = []
        vector_list2 = []
        similarity = VectorUtil.n_similarity(vector_list1, vector_list2)
    except:
        pass
```

## Method `compute_idf_weight_dict`

### Docstring

```python
@staticmethod
    def compute_idf_weight_dict(total_num, number_dict):
        """
        Calculate log(total_num+1/count+1) for each count in number_dict
        :param total_num: int
        :param number_dict: dict
        :return: dict
        >>> num_dict = {'key1':0.1, 'key2':0.5}
        >>> VectorUtil.compute_idf_weight_dict(2, num_dict)
        {'key1': 1.0033021088637848, 'key2': 0.6931471805599453}
        """
```

### Reference code (`solution_code`)

```python
@staticmethod
    def compute_idf_weight_dict(total_num, number_dict):
        index_2_key_map = {}

        index = 0

        count_list = []
        for key, count in number_dict.items():
            index_2_key_map[index] = key
            count_list.append(count)
            index = index + 1

        a = np.array(count_list)
        ## smooth, in case the divide by zero error
        a = np.log((total_num + 1) / (a + 1))
        result = {}

        for index, w in enumerate(a):
            key = index_2_key_map[index]
            result[key] = w

        return result
```

### Tests (`VectorUtilTestComputeIdfWeightDict`)

**test_compute_idf_weight_dict_1**: `stated`
- reason: The docstring's example uses the same inputs and expected values as the test, and the reference's log((total_num+1)/(count+1)) reproduces them, so a programmer following the docstring would pass.

```python
def test_compute_idf_weight_dict_1(self):
    num_dict = {'key1': 0.1, 'key2': 0.5}
    res = VectorUtil.compute_idf_weight_dict(2, num_dict)
    self.assertAlmostEqual(res['key1'], 1.0033021088637848)
    self.assertAlmostEqual(res['key2'], 0.6931471805599453)
```

**test_compute_idf_weight_dict_2**: `stated`
- reason: The docstring's formula, reinforced by its example (total 2, count 0.1 gives 1.0033), is log((total_num+1)/(count+1)), which yields the test's expected values of log(3/1.2) and log(3/1.5).

```python
def test_compute_idf_weight_dict_2(self):
    num_dict = {'key1': 0.2, 'key2': 0.5}
    res = VectorUtil.compute_idf_weight_dict(2, num_dict)
    self.assertAlmostEqual(res['key1'], 0.9162907318741551)
    self.assertAlmostEqual(res['key2'], 0.6931471805599453)
```

**test_compute_idf_weight_dict_3**: `stated`
- reason: The docstring's formula and worked example (2 with count 0.1 gives 1.0033) both match the natural log((total_num+1)/(count+1)) that the test checks with count 0.3, so a programmer following it would pass.

```python
def test_compute_idf_weight_dict_3(self):
    num_dict = {'key1': 0.3, 'key2': 0.5}
    res = VectorUtil.compute_idf_weight_dict(2, num_dict)
    self.assertAlmostEqual(res['key1'], 0.8362480242006185)
    self.assertAlmostEqual(res['key2'], 0.6931471805599453)
```

**test_compute_idf_weight_dict_4**: `stated`
- reason: The docstring's formula and its example (log((2+1)/(0.1+1)) ≈ 1.0033) both match the test's expected values for counts 0.4 and 0.5, so a programmer following it would pass.

```python
def test_compute_idf_weight_dict_4(self):
    num_dict = {'key1': 0.4, 'key2': 0.5}
    res = VectorUtil.compute_idf_weight_dict(2, num_dict)
    self.assertAlmostEqual(res['key1'], 0.7621400520468967)
    self.assertAlmostEqual(res['key2'], 0.6931471805599453)
```

**test_compute_idf_weight_dict_5**: `stated`
- reason: The docstring's formula log((total_num+1)/(count+1)) and its example (key1 = 0.1 giving 1.0033) fix the computation, so a programmer following it gets log(3/1.5) = 0.6931 for this test.

```python
def test_compute_idf_weight_dict_5(self):
    num_dict = {'key1': 0.5, 'key2': 0.5}
    res = VectorUtil.compute_idf_weight_dict(2, num_dict)
    self.assertAlmostEqual(res['key1'], 0.6931471805599453)
    self.assertAlmostEqual(res['key2'], 0.6931471805599453)
```

## Tests in no method's test class

### `VectorUtilTest`

**test_vectorutil**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_vectorutil(self):
    vector_1 = np.array([1, 1])
    vector_2 = np.array([1, 0])
    similarity = VectorUtil.similarity(vector_1, vector_2)
    self.assertAlmostEqual(similarity, 0.7071067811865475)

    vector1 = np.array([1, 1])
    vectors_all = [np.array([1, 0]), np.array([1, 1])]
    similarities = VectorUtil.cosine_similarities(vector1, vectors_all)
    res = [0.7071067811865475, 1.0]
    for index, item in enumerate(similarities):
        self.assertAlmostEqual(item, res[index])

    vector_list1 = [np.array([1, 0]), np.array([0, 1])]
    vector_list2 = [np.array([0, 0]), np.array([1, 1])]
    similarity = VectorUtil.n_similarity(vector_list1, vector_list2)
    self.assertAlmostEqual(similarity, 1.0)

    num_dict = {'key1': 0.1, 'key2': 0.5}
    res = VectorUtil.compute_idf_weight_dict(2, num_dict)
    self.assertAlmostEqual(res['key1'], 1.0033021088637848)
    self.assertAlmostEqual(res['key2'], 0.6931471805599453)
```
