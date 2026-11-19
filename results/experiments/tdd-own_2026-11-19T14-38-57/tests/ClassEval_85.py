import unittest


import unittest

class AgentTest_get_target_temperature(unittest.TestCase):

    def test_get_target_temperature_1(self):
        thermostat = Thermostat(20.4, 37.5, 'cool')
        self.assertEqual(thermostat.get_target_temperature(), 37.5)

    def test_get_target_temperature_2(self):
        thermostat = Thermostat(15.0, 22.0, 'heat')
        self.assertEqual(thermostat.get_target_temperature(), 22.0)

    def test_get_target_temperature_3(self):
        thermostat = Thermostat(30.0, 18.5, 'cool')
        self.assertEqual(thermostat.get_target_temperature(), 18.5)

    def test_get_target_temperature_4(self):
        thermostat = Thermostat(10.0, -5.5, 'heat')
        self.assertEqual(thermostat.get_target_temperature(), -5.5)

    def test_get_target_temperature_5(self):
        thermostat = Thermostat(20.0, 30.0, 'heat')
        first = thermostat.get_target_temperature()
        second = thermostat.get_target_temperature()
        self.assertEqual(first, 30.0)
        self.assertEqual(second, 30.0)
        self.assertEqual(first, thermostat.target_temperature)

import unittest

class AgentTest_set_target_temperature(unittest.TestCase):

    def test_set_target_temperature_1(self):
        thermostat = Thermostat(20.4, 37.5, 'cool')
        thermostat.set_target_temperature(37.6)
        self.assertEqual(thermostat.target_temperature, 37.6)

    def test_set_target_temperature_2(self):
        thermostat = Thermostat(15.0, 22.0, 'heat')
        thermostat.set_target_temperature(25.5)
        self.assertEqual(thermostat.target_temperature, 25.5)

    def test_set_target_temperature_3(self):
        thermostat = Thermostat(30.0, 18.5, 'cool')
        thermostat.set_target_temperature(-5.5)
        self.assertEqual(thermostat.target_temperature, -5.5)

    def test_set_target_temperature_4(self):
        thermostat = Thermostat(10.0, 20.0, 'heat')
        thermostat.set_target_temperature(30.0)
        thermostat.set_target_temperature(12.25)
        self.assertEqual(thermostat.target_temperature, 12.25)

    def test_set_target_temperature_5(self):
        thermostat = Thermostat(20.0, 30.0, 'heat')
        thermostat.set_target_temperature(35.0)
        self.assertEqual(thermostat.get_target_temperature(), 35.0)
        self.assertEqual(thermostat.target_temperature, 35.0)

import unittest

class AgentTest_get_mode(unittest.TestCase):

    def test_get_mode_1(self):
        thermostat = Thermostat(20.4, 37.5, 'cool')
        self.assertEqual(thermostat.get_mode(), 'cool')

    def test_get_mode_2(self):
        thermostat = Thermostat(15.0, 22.0, 'heat')
        self.assertEqual(thermostat.get_mode(), 'heat')

    def test_get_mode_3(self):
        thermostat = Thermostat(30.0, 18.5, 'cool')
        mode = thermostat.get_mode()
        self.assertIsInstance(mode, str)
        self.assertEqual(mode, 'cool')

    def test_get_mode_4(self):
        thermostat = Thermostat(10.0, -5.5, 'heat')
        thermostat.mode = 'cool'
        self.assertEqual(thermostat.get_mode(), 'cool')

    def test_get_mode_5(self):
        thermostat = Thermostat(20.0, 30.0, 'heat')
        first = thermostat.get_mode()
        second = thermostat.get_mode()
        self.assertEqual(first, 'heat')
        self.assertEqual(second, 'heat')
        self.assertEqual(first, thermostat.mode)

import unittest

class AgentTest_set_mode(unittest.TestCase):

    def test_set_mode_1(self):
        thermostat = Thermostat(20.4, 37.5, 'heat')
        thermostat.set_mode('cool')
        self.assertEqual(thermostat.mode, 'cool')

    def test_set_mode_2(self):
        thermostat = Thermostat(15.0, 22.0, 'cool')
        thermostat.set_mode('heat')
        self.assertEqual(thermostat.mode, 'heat')

    def test_set_mode_3(self):
        thermostat = Thermostat(20.0, 30.0, 'heat')
        thermostat.set_mode('heat')
        self.assertEqual(thermostat.mode, 'heat')
        self.assertEqual(thermostat.get_mode(), 'heat')

    def test_set_mode_4(self):
        thermostat = Thermostat(10.0, -5.5, 'heat')
        thermostat.set_mode('cool')
        self.assertEqual(thermostat.mode, 'cool')
        thermostat.set_mode('heat')
        self.assertEqual(thermostat.mode, 'heat')
        thermostat.set_mode('cool')
        self.assertEqual(thermostat.mode, 'cool')

    def test_set_mode_5(self):
        thermostat = Thermostat(20.4, 37.5, 'cool')
        thermostat.set_mode('heat')
        self.assertEqual(thermostat.get_mode(), 'heat')
        self.assertEqual(thermostat.current_temperature, 20.4)
        self.assertEqual(thermostat.target_temperature, 37.5)

import unittest

class AgentTest_auto_set_mode(unittest.TestCase):

    def test_auto_set_mode_1(self):
        thermostat = Thermostat(20.4, 37.5, 'cool')
        thermostat.auto_set_mode()
        self.assertEqual(thermostat.mode, 'heat')

    def test_auto_set_mode_2(self):
        thermostat = Thermostat(30.0, 18.5, 'heat')
        thermostat.auto_set_mode()
        self.assertEqual(thermostat.mode, 'cool')

    def test_auto_set_mode_3(self):
        thermostat = Thermostat(22.0, 22.0, 'heat')
        thermostat.auto_set_mode()
        self.assertEqual(thermostat.mode, 'cool')

    def test_auto_set_mode_4(self):
        thermostat = Thermostat(15.0, 22.0, 'cool')
        thermostat.auto_set_mode()
        self.assertEqual(thermostat.mode, 'heat')

    def test_auto_set_mode_5(self):
        thermostat = Thermostat(20.0, 30.0, 'cool')
        thermostat.set_target_temperature(10.0)
        thermostat.auto_set_mode()
        self.assertEqual(thermostat.mode, 'cool')
        self.assertEqual(thermostat.current_temperature, 20.0)
        self.assertEqual(thermostat.target_temperature, 10.0)

import unittest

class AgentTest_auto_check_conflict(unittest.TestCase):

    def test_auto_check_conflict_1(self):
        thermostat = Thermostat(20.4, 37.5, 'cool')
        result = thermostat.auto_check_conflict()
        self.assertFalse(result)
        self.assertEqual(thermostat.mode, 'heat')

    def test_auto_check_conflict_2(self):
        thermostat = Thermostat(15.0, 22.0, 'heat')
        result = thermostat.auto_check_conflict()
        self.assertTrue(result)
        self.assertEqual(thermostat.mode, 'heat')

    def test_auto_check_conflict_3(self):
        thermostat = Thermostat(30.0, 18.5, 'cool')
        result = thermostat.auto_check_conflict()
        self.assertTrue(result)
        self.assertEqual(thermostat.mode, 'cool')

    def test_auto_check_conflict_4(self):
        thermostat = Thermostat(30.0, 18.5, 'heat')
        result = thermostat.auto_check_conflict()
        self.assertFalse(result)
        self.assertEqual(thermostat.mode, 'cool')

    def test_auto_check_conflict_5(self):
        thermostat = Thermostat(10.0, -5.5, 'heat')
        first = thermostat.auto_check_conflict()
        self.assertFalse(first)
        self.assertEqual(thermostat.mode, 'cool')
        second = thermostat.auto_check_conflict()
        self.assertTrue(second)
        self.assertEqual(thermostat.mode, 'cool')
        self.assertEqual(thermostat.current_temperature, 10.0)
        self.assertEqual(thermostat.target_temperature, -5.5)

import unittest

class AgentTest_simulate_operation(unittest.TestCase):

    def test_simulate_operation_1(self):
        thermostat = Thermostat(20.4, 37.5, 'cool')
        self.assertEqual(thermostat.simulate_operation(), 18)

    def test_simulate_operation_2(self):
        thermostat = Thermostat(20.4, 37.5, 'cool')
        elapsed = thermostat.simulate_operation()
        self.assertIsInstance(elapsed, int)

    def test_simulate_operation_3(self):
        thermostat = Thermostat(20.4, 37.5, 'cool')
        thermostat.simulate_operation()
        self.assertGreaterEqual(thermostat.current_temperature, thermostat.target_temperature)
        self.assertEqual(thermostat.target_temperature, 37.5)

    def test_simulate_operation_4(self):
        thermostat = Thermostat(30.0, 18.5, 'heat')
        thermostat.simulate_operation()
        self.assertEqual(thermostat.mode, 'cool')
        self.assertLessEqual(thermostat.current_temperature, thermostat.target_temperature)

    def test_simulate_operation_5(self):
        thermostat = Thermostat(15.0, 22.0, 'cool')
        elapsed = thermostat.simulate_operation()
        self.assertEqual(thermostat.mode, 'heat')
        self.assertGreater(elapsed, 0)
        self.assertGreaterEqual(thermostat.current_temperature, 22.0)