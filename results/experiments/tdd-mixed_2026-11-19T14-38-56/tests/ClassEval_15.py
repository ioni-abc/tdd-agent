import unittest



class BoyerMooreSearchTestMatchInPattern(unittest.TestCase):
    def test_match_in_pattern(self):
        boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        self.assertEqual(boyerMooreSearch.match_in_pattern("A"), 0)

    def test_match_in_pattern_2(self):
        boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABAB")
        self.assertEqual(boyerMooreSearch.match_in_pattern("B"), 3)

    def test_match_in_pattern_3(self):
        boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABCABC")
        self.assertEqual(boyerMooreSearch.match_in_pattern("C"), 5)

import unittest

class AgentTest_match_in_pattern(unittest.TestCase):
    def test_match_in_pattern_1(self):
        boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABAB")
        self.assertEqual(boyerMooreSearch.match_in_pattern("A"), 2)

    def test_match_in_pattern_2(self):
        boyerMooreSearch = BoyerMooreSearch("XYZ", "Z")
        self.assertEqual(boyerMooreSearch.match_in_pattern("Z"), 0)

class BoyerMooreSearchTestMismatchInText(unittest.TestCase):
    def test_mismatch_in_text(self):
        boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        self.assertEqual(boyerMooreSearch.mismatch_in_text(0), -1)

    def test_mismatch_in_text_2(self):
        boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
        self.assertEqual(boyerMooreSearch.mismatch_in_text(0), 2)

    def test_mismatch_in_text_3(self):
        boyerMooreSearch = BoyerMooreSearch("AAAA", "ABC")
        self.assertEqual(boyerMooreSearch.mismatch_in_text(0), 2)

import unittest

class AgentTest_mismatch_in_text(unittest.TestCase):
    def test_mismatch_in_text_1(self):
        boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
        self.assertEqual(boyerMooreSearch.mismatch_in_text(3), 5)

    def test_mismatch_in_text_2(self):
        boyerMooreSearch = BoyerMooreSearch("ABAABA", "AAB")
        self.assertEqual(boyerMooreSearch.mismatch_in_text(2), -1)

class BoyerMooreSearchTestBadCharacterHeuristic(unittest.TestCase):
    def test_bad_character_heuristic(self):
        boyerMooreSearch = BoyerMooreSearch("ABAABA", "AB")
        self.assertEqual(boyerMooreSearch.bad_character_heuristic(), [0, 3])

    def test_bad_character_heuristic_2(self):
        boyerMooreSearch = BoyerMooreSearch("ABAABA", "ABC")
        self.assertEqual(boyerMooreSearch.bad_character_heuristic(), [])

    def test_bad_character_heuristic_3(self):
        boyerMooreSearch = BoyerMooreSearch("ABAABA", "")
        self.assertEqual(boyerMooreSearch.bad_character_heuristic(), [0, 1, 2, 3, 4, 5, 6])

import unittest

class AgentTest_bad_character_heuristic(unittest.TestCase):
    def test_bad_character_heuristic_1(self):
        boyerMooreSearch = BoyerMooreSearch("AAAA", "AA")
        self.assertEqual(boyerMooreSearch.bad_character_heuristic(), [0, 1, 2])

    def test_bad_character_heuristic_2(self):
        boyerMooreSearch = BoyerMooreSearch("XYZ", "Z")
        self.assertEqual(boyerMooreSearch.bad_character_heuristic(), [2])