import unittest


import unittest

class AgentTest_setNum(unittest.TestCase):

    def test_setNum_1(self):
        # Example from the docstring: 4 elements into 2 blocks, no remainder.
        a = AvgPartition([1, 2, 3, 4], 2)
        self.assertEqual(a.setNum(), (2, 0))

    def test_setNum_2(self):
        # 5 elements into 2 blocks: each block has 2, remainder 1.
        a = AvgPartition([1, 2, 3, 4, 5], 2)
        self.assertEqual(a.setNum(), (2, 1))

    def test_setNum_3(self):
        # More partitions than elements: each block size 0, remainder equals the length.
        a = AvgPartition([1, 2, 3], 5)
        self.assertEqual(a.setNum(), (0, 3))

    def test_setNum_4(self):
        # A single partition holds the whole list, so there is no remainder.
        a = AvgPartition([1, 2, 3, 4, 5, 6, 7], 1)
        self.assertEqual(a.setNum(), (7, 0))

    def test_setNum_5(self):
        # Empty list split into 3 blocks: size 0 and remainder 0.
        a = AvgPartition([], 3)
        self.assertEqual(a.setNum(), (0, 0))

import unittest

class AgentTest_get(unittest.TestCase):

    def test_get_1(self):
        # Docstring example: first block of 4 elements split into 2 blocks.
        a = AvgPartition([1, 2, 3, 4], 2)
        self.assertEqual(a.get(0), [1, 2])

    def test_get_2(self):
        # Second block of the same even split.
        a = AvgPartition([1, 2, 3, 4], 2)
        self.assertEqual(a.get(1), [3, 4])

    def test_get_3(self):
        # Even split into 3 blocks: first and last blocks.
        a = AvgPartition([1, 2, 3, 4, 5, 6], 3)
        self.assertEqual(a.get(0), [1, 2])
        self.assertEqual(a.get(2), [5, 6])

    def test_get_4(self):
        # Uneven split: 5 elements into 2 blocks. Blocks are contiguous, cover the
        # whole list in order, and their lengths are uniformly distributed (2 or 3).
        lst = [1, 2, 3, 4, 5]
        a = AvgPartition(lst, 2)
        first = a.get(0)
        second = a.get(1)
        self.assertIsInstance(first, list)
        self.assertIsInstance(second, list)
        self.assertEqual(first + second, lst)
        self.assertIn(len(first), (2, 3))
        self.assertIn(len(second), (2, 3))
        self.assertLessEqual(abs(len(first) - len(second)), 1)

    def test_get_5(self):
        # More partitions than elements: 3 elements into 5 blocks. Every block has
        # at most one element, and concatenating all blocks restores the list.
        lst = [1, 2, 3]
        a = AvgPartition(lst, 5)
        blocks = [a.get(i) for i in range(5)]
        for block in blocks:
            self.assertIsInstance(block, list)
            self.assertLessEqual(len(block), 1)
        combined = []
        for block in blocks:
            combined.extend(block)
        self.assertEqual(combined, lst)