import unittest


import unittest

import numpy as np

class AgentTest_similarity(unittest.TestCase):

    def test_similarity_1(self):
        # Example from the docstring: cos([1, 1], [1, 0]) = 1/sqrt(2)
        vector_1 = np.array([1, 1])
        vector_2 = np.array([1, 0])
        result = VectorUtil.similarity(vector_1, vector_2)
        self.assertAlmostEqual(float(result), 0.7071067811865475, places=7)

    def test_similarity_2(self):
        # Identical non-zero vectors have cosine similarity 1
        vector_1 = np.array([3.0, -2.0, 5.0])
        vector_2 = np.array([3.0, -2.0, 5.0])
        result = VectorUtil.similarity(vector_1, vector_2)
        self.assertAlmostEqual(float(result), 1.0, places=7)

    def test_similarity_3(self):
        # Orthogonal vectors have cosine similarity 0
        vector_1 = np.array([1.0, 0.0, 0.0])
        vector_2 = np.array([0.0, 4.0, 0.0])
        result = VectorUtil.similarity(vector_1, vector_2)
        self.assertAlmostEqual(float(result), 0.0, places=7)

    def test_similarity_4(self):
        # Vectors pointing in opposite directions have cosine similarity -1
        vector_1 = np.array([1.0, 2.0, 3.0])
        vector_2 = np.array([-2.0, -4.0, -6.0])
        result = VectorUtil.similarity(vector_1, vector_2)
        self.assertAlmostEqual(float(result), -1.0, places=7)

    def test_similarity_5(self):
        # General case: cosine similarity of [1, 2, 3] and [4, 5, 6] is
        # 32 / (sqrt(14) * sqrt(77)); it is symmetric and independent of vector length
        vector_1 = np.array([1.0, 2.0, 3.0])
        vector_2 = np.array([4.0, 5.0, 6.0])
        expected = 32.0 / (np.sqrt(14.0) * np.sqrt(77.0))

        forward = float(VectorUtil.similarity(vector_1, vector_2))
        backward = float(VectorUtil.similarity(vector_2, vector_1))
        scaled = float(VectorUtil.similarity(10.0 * vector_1, vector_2))

        self.assertAlmostEqual(forward, expected, places=7)
        self.assertAlmostEqual(backward, expected, places=7)
        self.assertAlmostEqual(scaled, expected, places=7)

import unittest

import numpy as np

class AgentTest_cosine_similarities(unittest.TestCase):

    def test_cosine_similarities_1(self):
        # Docstring example: cosine of [1, 2, 3] with each row of vectors_all
        vector1 = np.array([1, 2, 3])
        vectors_all = [np.array([4, 5, 6]), np.array([7, 8, 9])]
        result = np.asarray(VectorUtil.cosine_similarities(vector1, vectors_all))
        expected = np.array([0.97463185, 0.95941195])
        self.assertEqual(result.shape, (2,))
        np.testing.assert_allclose(result, expected, rtol=0, atol=1e-6)

    def test_cosine_similarities_2(self):
        # Output has shape (num_vectors,) for a larger set of vectors
        vector_1 = np.array([1.0, 0.0, 2.0, -1.0])
        vectors_all = [
            np.array([1.0, 1.0, 1.0, 1.0]),
            np.array([0.0, 3.0, 0.0, 2.0]),
            np.array([-2.0, 4.0, 1.0, 0.5]),
            np.array([5.0, -1.0, 0.0, 0.0]),
            np.array([1.0, 2.0, 3.0, 4.0]),
        ]
        result = np.asarray(VectorUtil.cosine_similarities(vector_1, vectors_all))
        self.assertEqual(result.shape, (5,))

    def test_cosine_similarities_3(self):
        # Identical row -> 1, opposite row -> -1, orthogonal row -> 0
        vector_1 = np.array([3.0, -2.0, 5.0])
        vectors_all = [
            np.array([3.0, -2.0, 5.0]),
            np.array([-6.0, 4.0, -10.0]),
            np.array([10.0, 15.0, 0.0]),
        ]
        result = np.asarray(VectorUtil.cosine_similarities(vector_1, vectors_all))
        np.testing.assert_allclose(result, np.array([1.0, -1.0, 0.0]), rtol=0, atol=1e-7)

    def test_cosine_similarities_4(self):
        # Each entry equals the cosine similarity between vector_1 and that row
        vector_1 = np.array([1.0, 2.0, 3.0])
        vectors_all = [
            np.array([4.0, 5.0, 6.0]),
            np.array([-1.0, 0.5, 2.0]),
            np.array([0.0, 0.0, 1.0]),
        ]
        result = np.asarray(VectorUtil.cosine_similarities(vector_1, vectors_all))
        for i, row in enumerate(vectors_all):
            expected = float(VectorUtil.similarity(vector_1, row))
            self.assertAlmostEqual(float(result[i]), expected, places=7)

    def test_cosine_similarities_5(self):
        # Cosine similarity is independent of vector length: scaling a row
        # in vectors_all does not change its entry in the result
        vector_1 = np.array([1.0, 2.0, 3.0])
        base_row = np.array([4.0, 5.0, 6.0])
        other_row = np.array([7.0, 8.0, 9.0])

        original = np.asarray(
            VectorUtil.cosine_similarities(vector_1, [base_row, other_row])
        )
        scaled = np.asarray(
            VectorUtil.cosine_similarities(vector_1, [100.0 * base_row, 0.01 * other_row])
        )
        np.testing.assert_allclose(scaled, original, rtol=0, atol=1e-7)

import unittest

import numpy as np

class AgentTest_n_similarity(unittest.TestCase):

    def test_n_similarity_1(self):
        # Docstring example: vector_list1 = [[1,2,3],[4,5,6]],
        # vector_list2 = [[7,8,9],[10,11,12]] gives 0.9897287473881233
        vector_list1 = [np.array([1, 2, 3]), np.array([4, 5, 6])]
        vector_list2 = [np.array([7, 8, 9]), np.array([10, 11, 12])]
        result = VectorUtil.n_similarity(vector_list1, vector_list2)
        self.assertAlmostEqual(float(np.asarray(result).ravel()[0]), 0.9897287473881233, places=6)

    def test_n_similarity_2(self):
        # Identical sets of vectors have similarity 1
        vector_list1 = [np.array([3.0, -2.0, 5.0]), np.array([1.0, 4.0, -1.0])]
        vector_list2 = [np.array([3.0, -2.0, 5.0]), np.array([1.0, 4.0, -1.0])]
        result = VectorUtil.n_similarity(vector_list1, vector_list2)
        self.assertAlmostEqual(float(np.asarray(result).ravel()[0]), 1.0, places=7)

    def test_n_similarity_3(self):
        # Sets pointing in opposite directions have similarity -1
        vector_list1 = [np.array([1.0, 0.0]), np.array([3.0, 0.0])]
        vector_list2 = [np.array([-2.0, 0.0])]
        result = VectorUtil.n_similarity(vector_list1, vector_list2)
        self.assertAlmostEqual(float(np.asarray(result).ravel()[0]), -1.0, places=7)

    def test_n_similarity_4(self):
        # Orthogonal sets have similarity 0
        vector_list1 = [np.array([1.0, 0.0]), np.array([1.0, 0.0])]
        vector_list2 = [np.array([0.0, 2.0])]
        result = VectorUtil.n_similarity(vector_list1, vector_list2)
        self.assertAlmostEqual(float(np.asarray(result).ravel()[0]), 0.0, places=7)

    def test_n_similarity_5(self):
        # Repeating a vector within a list does not change the similarity:
        # n_similarity([v1], [v2, v2]) equals similarity(v1, v2)
        v1 = np.array([1.0, 2.0, 3.0])
        v2 = np.array([4.0, 5.0, 6.0])
        expected = 32.0 / (np.sqrt(14.0) * np.sqrt(77.0))
        result = VectorUtil.n_similarity([v1], [v2, v2])
        self.assertAlmostEqual(float(np.asarray(result).ravel()[0]), expected, places=7)

import math

import unittest

import numpy as np

class AgentTest_compute_idf_weight_dict(unittest.TestCase):

    def test_compute_idf_weight_dict_1(self):
        # Docstring example: total_num=2, number_dict={'key1': 0.1, 'key2': 0.5}
        # gives log((2+1)/(0.1+1)) and log((2+1)/(0.5+1)) = log(2)
        num_dict = {'key1': 0.1, 'key2': 0.5}
        result = VectorUtil.compute_idf_weight_dict(2, num_dict)
        self.assertIsInstance(result, dict)
        self.assertEqual(set(result.keys()), {'key1', 'key2'})
        self.assertAlmostEqual(float(result['key1']), 1.0033021088637848, places=7)
        self.assertAlmostEqual(float(result['key2']), 0.6931471805599453, places=7)

    def test_compute_idf_weight_dict_2(self):
        # An empty number_dict yields an empty dict
        result = VectorUtil.compute_idf_weight_dict(10, {})
        self.assertIsInstance(result, dict)
        self.assertEqual(result, {})

    def test_compute_idf_weight_dict_3(self):
        # When count equals total_num, (total_num+1)/(count+1) = 1, so the weight is log(1) = 0
        num_dict = {'a': 4, 'b': 4.0}
        result = VectorUtil.compute_idf_weight_dict(4, num_dict)
        self.assertEqual(set(result.keys()), {'a', 'b'})
        self.assertAlmostEqual(float(result['a']), 0.0, places=7)
        self.assertAlmostEqual(float(result['b']), 0.0, places=7)

    def test_compute_idf_weight_dict_4(self):
        # Edge values: total_num=0 and count=0 gives log(1/1) = 0;
        # total_num=0 and count=1 gives log(1/2)
        result = VectorUtil.compute_idf_weight_dict(0, {'zero': 0, 'one': 1})
        self.assertAlmostEqual(float(result['zero']), 0.0, places=7)
        self.assertAlmostEqual(float(result['one']), math.log(0.5), places=7)

    def test_compute_idf_weight_dict_5(self):
        # Integer counts: total_num=9 gives log((9+1)/(count+1)) for each count
        num_dict = {'x': 2, 'y': 0, 'z': 99}
        result = VectorUtil.compute_idf_weight_dict(9, num_dict)
        self.assertEqual(set(result.keys()), {'x', 'y', 'z'})
        self.assertAlmostEqual(float(result['x']), math.log(10.0 / 3.0), places=7)
        self.assertAlmostEqual(float(result['y']), math.log(10.0 / 1.0), places=7)
        self.assertAlmostEqual(float(result['z']), math.log(10.0 / 100.0), places=7)