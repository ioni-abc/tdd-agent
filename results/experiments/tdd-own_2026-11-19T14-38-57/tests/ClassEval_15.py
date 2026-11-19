import unittest


import unittest

class AgentTest_match_in_pattern(unittest.TestCase):

    def test_match_in_pattern_1(self):
        # Docstring example: "A" occurs only at index 0 of the pattern "AB".
        boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        self.assertEqual(boyerMooreSearch.match_in_pattern("A"), 0)

    def test_match_in_pattern_2(self):
        # Single occurrence of "B" in "AB" is at index 1.
        boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        self.assertEqual(boyerMooreSearch.match_in_pattern("B"), 1)

    def test_match_in_pattern_3(self):
        # "A" appears at indices 0 and 3; the rightmost is 3.
        boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABCAB")
        self.assertEqual(boyerMooreSearch.match_in_pattern("A"), 3)

    def test_match_in_pattern_4(self):
        # "B" appears at indices 1 and 4; the rightmost is 4.
        boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABCAB")
        self.assertEqual(boyerMooreSearch.match_in_pattern("B"), 4)

    def test_match_in_pattern_5(self):
        # Repeated character throughout the pattern; the rightmost index is the last one.
        boyerMooreSearch = BoyerMooreSearch("AAAAAA", "AAAA")
        self.assertEqual(boyerMooreSearch.match_in_pattern("A"), 3)

import unittest

class AgentTest_mismatch_in_text(unittest.TestCase):

    def test_mismatch_in_text_1(self):
        # Docstring example: aligning "ABC" at position 0 of "ABAABA" mismatches at text index 2.
        boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
        self.assertEqual(boyerMooreSearch.mismatch_in_text(0), 2)

    def test_mismatch_in_text_2(self):
        # "AB" fully matches "ABAABA" at position 0, so there is no mismatch.
        boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        self.assertEqual(boyerMooreSearch.mismatch_in_text(0), -1)

    def test_mismatch_in_text_3(self):
        # "AB" matches "ABAABA" at position 3 ("AB" at indices 3-4), so there is no mismatch.
        boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        self.assertEqual(boyerMooreSearch.mismatch_in_text(3), -1)

    def test_mismatch_in_text_4(self):
        # Only the first pattern character differs from the text (text index 0).
        boyerMooreSearch = BoyerMooreSearch("XBCD", "ABCD")
        self.assertEqual(boyerMooreSearch.mismatch_in_text(0), 0)

    def test_mismatch_in_text_5(self):
        # Only the last pattern character differs: pattern "ABCDX" vs text "ABCDE" mismatches at index 4.
        boyerMooreSearch = BoyerMooreSearch("ABCDE", "ABCDX")
        self.assertEqual(boyerMooreSearch.mismatch_in_text(0), 4)

import unittest

class AgentTest_bad_character_heuristic(unittest.TestCase):

    def test_bad_character_heuristic_1(self):
        # Docstring example: "AB" occurs in "ABAABA" at positions 0 and 3.
        boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        self.assertEqual(boyerMooreSearch.bad_character_heuristic(), [0, 3])

    def test_bad_character_heuristic_2(self):
        # The pattern "XY" does not occur anywhere in "ABCDEF", so the result is empty.
        boyerMooreSearch = BoyerMooreSearch("ABCDEF", "XY")
        self.assertEqual(boyerMooreSearch.bad_character_heuristic(), [])

    def test_bad_character_heuristic_3(self):
        # A single occurrence of "LD" at the end of "HELLOWORLD" (index 8).
        boyerMooreSearch = BoyerMooreSearch("HELLOWORLD", "LD")
        self.assertEqual(boyerMooreSearch.bad_character_heuristic(), [8])

    def test_bad_character_heuristic_4(self):
        # Overlapping occurrences of "AA" in "AAAA" are all reported: positions 0, 1 and 2.
        boyerMooreSearch = BoyerMooreSearch("AAAA", "AA")
        self.assertEqual(boyerMooreSearch.bad_character_heuristic(), [0, 1, 2])

    def test_bad_character_heuristic_5(self):
        # When the pattern equals the whole text, the only occurrence is at position 0.
        boyerMooreSearch = BoyerMooreSearch("ABC", "ABC")
        self.assertEqual(boyerMooreSearch.bad_character_heuristic(), [0])