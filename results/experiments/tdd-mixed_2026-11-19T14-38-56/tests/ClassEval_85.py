import unittest



class ThermostatTestGetTargetTemperature(unittest.TestCase):
    def test_get_target_temperature_1(self):
        t = Thermostat(20, 25, 'heat')
        self.assertEqual(t.get_target_temperature(), 25)

    def test_get_target_temperature_2(self):
        t = Thermostat(20, 25, 'cool')
        self.assertEqual(t.get_target_temperature(), 25)

    def test_get_target_temperature_3(self):
        t = Thermostat(20, 25, 'test')
        self.assertEqual(t.get_target_temperature(), 25)

import unittest

class AgentTest_get_target_temperature(unittest.TestCase):
    def test_get_target_temperature_1(self):
        thermostat = Thermostat(20.4, 37.5, 'cool')
        self.assertEqual(thermostat.get_target_temperature(), 37.5)

    def test_get_target_temperature_2(self):
        thermostat = Thermostat(-5.5, 0.0, 'heat')
        self.assertEqual(thermostat.get_target_temperature(), 0.0)
        self.assertNotEqual(thermostat.get_target_temperature(), -5.5)

class ThermostatTestSetTargetTemperature(unittest.TestCase):
    def test_set_target_temperature_1(self):
        t = Thermostat(20, 25, 'heat')
        t.set_target_temperature(30)
        self.assertEqual(t.get_target_temperature(), 30)

    def test_set_target_temperature_2(self):
        t = Thermostat(20, 25, 'cool')
        t.set_target_temperature(10)
        self.assertEqual(t.get_target_temperature(), 10)

    def test_set_target_temperature_3(self):
        t = Thermostat(20, 25, 'test')
        t.set_target_temperature(10)
        self.assertEqual(t.get_target_temperature(), 10)

import unittest

class AgentTest_set_target_temperature(unittest.TestCase):
    def test_set_target_temperature_1(self):
        thermostat = Thermostat(20.4, 37.5, 'cool')
        thermostat.set_target_temperature(37.6)
        self.assertEqual(thermostat.target_temperature, 37.6)

    def test_set_target_temperature_2(self):
        thermostat = Thermostat(20.4, 37.5, 'heat')
        thermostat.set_target_temperature(25.0)
        self.assertEqual(thermostat.current_temperature, 20.4)
        self.assertEqual(thermostat.mode, 'heat')

class ThermostatTestGetMode(unittest.TestCase):
    def test_get_mode_1(self):
        t = Thermostat(20, 25, 'heat')
        self.assertEqual(t.get_mode(), 'heat')

    def test_get_mode_2(self):
        t = Thermostat(20, 25, 'cool')
        self.assertEqual(t.get_mode(), 'cool')

    def test_get_mode_3(self):
        t = Thermostat(20, 25, 'test')
        self.assertEqual(t.get_mode(), 'test')

import unittest

class AgentTest_get_mode(unittest.TestCase):
    def test_get_mode_1(self):
        thermostat = Thermostat(20.4, 37.5, 'heat')
        thermostat.set_mode('cool')
        self.assertEqual(thermostat.get_mode(), 'cool')

    def test_get_mode_2(self):
        thermostat = Thermostat(20.4, 37.5, 'cool')
        thermostat.auto_set_mode()
        self.assertEqual(thermostat.get_mode(), 'heat')

class ThermostatTestSetMode(unittest.TestCase):
    def test_set_mode_1(self):
        t = Thermostat(20, 25, 'heat')
        t.set_mode('cool')
        self.assertEqual(t.get_mode(), 'cool')

    def test_set_mode_2(self):
        t = Thermostat(20, 25, 'heat')
        self.assertFalse(t.set_mode('test'))

    def test_set_mode_3(self):
        t = Thermostat(20, 25, 'cool')
        t.set_mode('heat')
        self.assertEqual(t.get_mode(), 'heat')

class AgentTest_set_mode(unittest.TestCase):
    def test_set_mode_1(self):
        thermostat = Thermostat(20.4, 37.5, 'heat')
        thermostat.set_mode('cool')
        self.assertEqual(thermostat.mode, 'cool')

    def test_set_mode_2(self):
        thermostat = Thermostat(20.4, 37.5, 'heat')
        thermostat.set_mode('cool')
        self.assertEqual(thermostat.current_temperature, 20.4)
        self.assertEqual(thermostat.target_temperature, 37.5)

class ThermostatTestAutoSetMode(unittest.TestCase):
    def test_auto_set_mode_1(self):
        t = Thermostat(20, 25, 'heat')
        t.auto_set_mode()
        self.assertEqual(t.get_mode(), 'heat')

    def test_auto_set_mode_2(self):
        t = Thermostat(25, 20, 'heat')
        t.auto_set_mode()
        self.assertEqual(t.get_mode(), 'cool')

    def test_auto_set_mode_3(self):
        t = Thermostat(25, 20, 'cool')
        t.auto_set_mode()
        self.assertEqual(t.get_mode(), 'cool')

class AgentTest_auto_set_mode(unittest.TestCase):
    def test_auto_set_mode_1(self):
        thermostat = Thermostat(20.4, 37.5, 'cool')
        thermostat.auto_set_mode()
        self.assertEqual(thermostat.mode, 'heat')

    def test_auto_set_mode_2(self):
        thermostat = Thermostat(25.0, 25.0, 'heat')
        thermostat.auto_set_mode()
        self.assertEqual(thermostat.mode, 'cool')

class ThermostatTestAutoCheckConflict(unittest.TestCase):
    def test_auto_check_conflict_1(self):
        t = Thermostat(30, 25, 'cool')
        self.assertTrue(t.auto_check_conflict())

    def test_auto_check_conflict_2(self):
        t = Thermostat(30, 25, 'heat')
        self.assertFalse(t.auto_check_conflict())
        self.assertEqual(t.mode, 'cool')

    def test_auto_check_conflict_3(self):
        t = Thermostat(25, 30, 'heat')
        self.assertTrue(t.auto_check_conflict())

import unittest

class AgentTest_auto_check_conflict(unittest.TestCase):
    def test_auto_check_conflict_1(self):
        thermostat = Thermostat(20.4, 37.5, 'cool')
        self.assertFalse(thermostat.auto_check_conflict())
        self.assertEqual(thermostat.mode, 'heat')

    def test_auto_check_conflict_2(self):
        thermostat = Thermostat(25.0, 20.0, 'cool')
        self.assertTrue(thermostat.auto_check_conflict())
        self.assertEqual(thermostat.mode, 'cool')
        self.assertEqual(thermostat.current_temperature, 25.0)
        self.assertEqual(thermostat.target_temperature, 20.0)

class ThermostatTestSimulateOperation(unittest.TestCase):
    def test_simulate_operation_1(self):
        t = Thermostat(20, 25, 'heat')
        self.assertEqual(t.simulate_operation(), 5)
        self.assertEqual(t.get_mode(), 'heat')
        self.assertEqual(t.current_temperature, 25)

    def test_simulate_operation_2(self):
        t = Thermostat(25.7, 20, 'cool')
        self.assertEqual(t.simulate_operation(), 6)
        self.assertEqual(t.get_mode(), 'cool')
        self.assertEqual(t.current_temperature, 19.7)

    def test_simulate_operation_3(self):
        t = Thermostat(25, 25, 'heat')
        self.assertEqual(t.simulate_operation(), 0)
        self.assertEqual(t.get_mode(), 'cool')
        self.assertEqual(t.current_temperature, 25)

import unittest

class AgentTest_simulate_operation(unittest.TestCase):
    def test_simulate_operation_1(self):
        thermostat = Thermostat(20.4, 37.5, 'cool')
        self.assertEqual(thermostat.simulate_operation(), 18)
        self.assertEqual(thermostat.mode, 'heat')
        self.assertGreaterEqual(thermostat.current_temperature, 37.5)

    def test_simulate_operation_2(self):
        thermostat = Thermostat(30, 25, 'heat')
        elapsed = thermostat.simulate_operation()
        self.assertIsInstance(elapsed, int)
        self.assertEqual(elapsed, 5)
        self.assertEqual(thermostat.mode, 'cool')
        self.assertLessEqual(thermostat.current_temperature, 25)