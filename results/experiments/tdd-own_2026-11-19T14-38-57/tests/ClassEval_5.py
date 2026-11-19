import unittest


import io

import unittest

from contextlib import redirect_stdout

class AgentTest_display(unittest.TestCase):

    def _capture_display(self, key, value):
        context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            context.display(key, value)
        return buffer.getvalue().strip()

    def test_display_1(self):
        output = self._capture_display("C", "53231323")
        self.assertEqual(
            output,
            "Normal Guitar Playing -- Chord: C, Play Tune: 53231323"
        )

    def test_display_2(self):
        output = self._capture_display("Em", "43231323")
        self.assertEqual(
            output,
            "Normal Guitar Playing -- Chord: Em, Play Tune: 43231323"
        )

    def test_display_3(self):
        output = self._capture_display("G", "63231323")
        self.assertEqual(
            output,
            "Normal Guitar Playing -- Chord: G, Play Tune: 63231323"
        )

    def test_display_4(self):
        output = self._capture_display("F", "43231323")
        self.assertTrue(
            output.startswith("Normal Guitar Playing -- Chord: F, Play Tune: ")
        )
        self.assertIn("Play Tune: 43231323", output)
        self.assertEqual(len(output.splitlines()), 1)

    def test_display_5(self):
        output = self._capture_display("F#m", "1234")
        self.assertEqual(
            output,
            "Normal Guitar Playing -- Chord: F#m, Play Tune: 1234"
        )

import io

import unittest

from contextlib import redirect_stdout

class AgentTest_interpret(unittest.TestCase):

    def test_interpret_1(self):
        context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        play_list = context.interpret(display=False)
        self.assertEqual(
            play_list,
            [
                {'Chord': 'C', 'Tune': '53231323'},
                {'Chord': 'Em', 'Tune': '43231323'},
                {'Chord': 'F', 'Tune': '43231323'},
                {'Chord': 'G', 'Tune': '63231323'},
            ]
        )

    def test_interpret_2(self):
        context = AutomaticGuitarSimulator("")
        self.assertEqual(context.interpret(), [])

    def test_interpret_3(self):
        context = AutomaticGuitarSimulator("   \t \n  ")
        self.assertEqual(context.interpret(), [])

    def test_interpret_4(self):
        context = AutomaticGuitarSimulator("Dm12")
        self.assertEqual(
            context.interpret(),
            [{'Chord': 'Dm', 'Tune': '12'}]
        )

    def test_interpret_5(self):
        text = "C53231323 Em43231323 F43231323 G63231323"
        expected = [
            {'Chord': 'C', 'Tune': '53231323'},
            {'Chord': 'Em', 'Tune': '43231323'},
            {'Chord': 'F', 'Tune': '43231323'},
            {'Chord': 'G', 'Tune': '63231323'},
        ]
        context = AutomaticGuitarSimulator(text)
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            result = context.interpret(display=True)
        self.assertEqual(result, expected)