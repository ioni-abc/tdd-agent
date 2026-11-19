import unittest




class AutomaticGuitarSimulatorTestDisplay(unittest.TestCase):
    def test_display_1(self):
        context = AutomaticGuitarSimulator("C53231323 Em43231323")
        play_list = context.interpret()
        str = context.display(play_list[0]['Chord'], play_list[0]['Tune'])
        self.assertEqual(str, "Normal Guitar Playing -- Chord: C, Play Tune: 53231323")

    def test_display_2(self):
        context = AutomaticGuitarSimulator("C53231323 Em43231323")
        play_list = context.interpret()
        str = context.display(play_list[1]['Chord'], play_list[1]['Tune'])
        self.assertEqual(str, "Normal Guitar Playing -- Chord: Em, Play Tune: 43231323")

    def test_display_3(self):
        context = AutomaticGuitarSimulator("F43231323 G63231323")
        play_list = context.interpret()
        str = context.display(play_list[0]['Chord'], play_list[0]['Tune'])
        self.assertEqual(str, "Normal Guitar Playing -- Chord: F, Play Tune: 43231323")

import unittest

class AgentTest_display(unittest.TestCase):
    def test_display_4(self):
        context = AutomaticGuitarSimulator("Am22000200")
        result = context.display("Am", "0")
        self.assertEqual(result, "Normal Guitar Playing -- Chord: Am, Play Tune: 0")

    def test_display_5(self):
        context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        play_list = context.interpret()
        result = context.display(play_list[3]['Chord'], play_list[3]['Tune'])
        self.assertIsInstance(result, str)
        self.assertEqual(result, "Normal Guitar Playing -- Chord: G, Play Tune: 63231323")

class AutomaticGuitarSimulatorTestInterpret(unittest.TestCase):
    def test_interpret_1(self):
        context = AutomaticGuitarSimulator("C53231323")
        play_list = context.interpret()
        self.assertEqual(play_list, [{'Chord': 'C', 'Tune': '53231323'}])

    def test_interpret_2(self):
        context = AutomaticGuitarSimulator("F43231323")
        play_list = context.interpret()
        self.assertEqual(play_list, [{'Chord': 'F', 'Tune': '43231323'}])

    def test_interpret_3(self):
        context = AutomaticGuitarSimulator("Em43231323")
        play_list = context.interpret()
        self.assertEqual(play_list, [{'Chord': 'Em', 'Tune': '43231323'}])

    def test_interpret_4(self):
        context = AutomaticGuitarSimulator("G63231323")
        play_list = context.interpret()
        self.assertEqual(play_list, [{'Chord': 'G', 'Tune': '63231323'}])

    def test_interpret_5(self):
        context = AutomaticGuitarSimulator("F43231323 G63231323")
        play_list = context.interpret()
        self.assertEqual(play_list, [{'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}])

    def test_interpret_6(self):
        context = AutomaticGuitarSimulator(" ")
        play_list = context.interpret()
        self.assertEqual(play_list, [])

import unittest

class AgentTest_interpret(unittest.TestCase):
    def test_interpret_1(self):
        context = AutomaticGuitarSimulator("")
        play_list = context.interpret()
        self.assertEqual(play_list, [])

    def test_interpret_2(self):
        context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        play_list = context.interpret(display=False)
        self.assertEqual(play_list, [
            {'Chord': 'C', 'Tune': '53231323'},
            {'Chord': 'Em', 'Tune': '43231323'},
            {'Chord': 'F', 'Tune': '43231323'},
            {'Chord': 'G', 'Tune': '63231323'}
        ])

    def test_interpret_3(self):
        context = AutomaticGuitarSimulator("Am22000200")
        play_list = context.interpret()
        self.assertEqual(play_list, [{'Chord': 'Am', 'Tune': '22000200'}])