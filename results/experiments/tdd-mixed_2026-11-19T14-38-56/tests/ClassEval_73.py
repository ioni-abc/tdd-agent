import unittest



class RPGCharacterTestAttack(unittest.TestCase):
    def test_attack(self):
        character1 = RPGCharacter("John", 100, 20, 10)
        character2 = RPGCharacter("Enemy", 100, 15, 5)
        character1.attack(character2)
        self.assertEqual(character2.hp, 85)

    def test_attack_2(self):
        character1 = RPGCharacter("John", 100, 20, 10)
        character2 = RPGCharacter("Enemy", 100, 15, 5)
        character2.attack(character1)
        self.assertEqual(character1.hp, 95)

    def test_attack_3(self):
        character1 = RPGCharacter("John", 100, 20, 10)
        character2 = RPGCharacter("Enemy", 100, 15, 5)
        character1.attack(character2)
        character2.attack(character1)
        self.assertEqual(character1.hp, 95)
        self.assertEqual(character2.hp, 85)

import unittest

class AgentTest_attack(unittest.TestCase):
    def test_attack_1(self):
        player_1 = RPGCharacter('player 1', 100, 10, 3)
        player_2 = RPGCharacter('player 2', 100, 7, 2)
        player_1.attack(player_2)
        self.assertEqual(player_2.hp, 92)

    def test_attack_2(self):
        attacker = RPGCharacter("Attacker", 100, 30, 10)
        defender = RPGCharacter("Defender", 80, 12, 6)
        result = attacker.attack(defender)
        self.assertIsNone(result)
        self.assertEqual(attacker.hp, 100)
        self.assertEqual(defender.hp, 76)

class RPGCharacterTestHeal(unittest.TestCase):
    def test_heal_1(self):
        character = RPGCharacter("John", 90, 20, 10)
        character.heal()
        self.assertEqual(character.hp, 100)

    def test_heal_2(self):
        character = RPGCharacter("John", 97, 20, 10)
        character.heal()
        self.assertEqual(character.hp, 100)

    def test_heal_3(self):
        character = RPGCharacter("John", 100, 20, 10)
        character.heal()
        self.assertEqual(character.hp, 100)

import unittest

class AgentTest_heal(unittest.TestCase):
    def test_heal_1(self):
        character = RPGCharacter("John", 50, 20, 10)
        result = character.heal()
        self.assertEqual(character.hp, 60)
        self.assertEqual(result, 60)

    def test_heal_2(self):
        character = RPGCharacter("John", 93, 10, 3)
        result = character.heal()
        self.assertEqual(result, 100)
        self.assertEqual(character.hp, 100)

class RPGCharacterTestLevelUp(unittest.TestCase):
    def test_level_up_1(self):
        character = RPGCharacter("John", 100, 20, 10)
        character.level_up()
        self.assertEqual(character.level, 2)
        self.assertEqual(character.exp, 0)
        self.assertEqual(character.hp, 120)
        self.assertEqual(character.attack_power, 25)
        self.assertEqual(character.defense, 15)

    def test_level_up_2(self):
        character = RPGCharacter("John", 100, 20, 10, 100)
        character.level_up()
        self.assertEqual(character.level, 100)
        self.assertEqual(character.exp, 0)
        self.assertEqual(character.hp, 100)
        self.assertEqual(character.attack_power, 20)
        self.assertEqual(character.defense, 10)

    def test_level_up_3(self):
        character = RPGCharacter("John", 100, 20, 10, 2)
        character.level_up()
        self.assertEqual(character.level, 3)
        self.assertEqual(character.exp, 0)
        self.assertEqual(character.hp, 120)
        self.assertEqual(character.attack_power, 25)
        self.assertEqual(character.defense, 15)

import unittest

class AgentTest_level_up(unittest.TestCase):
    def test_level_up_1(self):
        character = RPGCharacter('player 1', 100, 10, 3)
        result = character.level_up()
        self.assertEqual(result, (2, 120, 15, 8))
        self.assertEqual(character.level, 2)
        self.assertEqual(character.hp, 120)
        self.assertEqual(character.attack_power, 15)
        self.assertEqual(character.defense, 8)

    def test_level_up_2(self):
        character = RPGCharacter('player 2', 100, 20, 10, 99)
        result = character.level_up()
        self.assertEqual(result, (100, 120, 25, 15))
        self.assertEqual(character.level, 100)
        self.assertEqual(character.exp, 0)
        self.assertEqual(character.hp, 120)
        self.assertEqual(character.attack_power, 25)
        self.assertEqual(character.defense, 15)

class RPGCharacterTestGainExp(unittest.TestCase):

    # exp not overflow
    def test_gain_exp_1(self):
        character = RPGCharacter("John", 100, 20, 10)
        character.gain_exp(100)
        self.assertEqual(character.level, 2)
        self.assertEqual(character.exp, 0)

    def test_gain_exp_2(self):
        character = RPGCharacter("John", 100, 20, 10)
        character.gain_exp(1100)
        self.assertEqual(character.level, 5)
        self.assertEqual(character.exp, 100)

    def test_gain_exp_3(self):
        character = RPGCharacter("John", 100, 20, 10)
        character.gain_exp(200)
        self.assertEqual(character.level, 2)
        self.assertEqual(character.exp, 100)

class AgentTest_gain_exp(unittest.TestCase):
    def test_gain_exp_1(self):
        character = RPGCharacter('player 1', 100, 10, 3)
        character.gain_exp(50)
        self.assertEqual(character.level, 1)
        self.assertEqual(character.exp, 50)

    def test_gain_exp_2(self):
        character = RPGCharacter('player 1', 100, 10, 3)
        character.gain_exp(60)
        character.gain_exp(60)
        self.assertEqual(character.level, 2)
        self.assertEqual(character.exp, 20)

class RPGCharacterTestIsAlive(unittest.TestCase):
    def test_is_alive_1(self):
        character = RPGCharacter("John", 100, 20, 10)
        self.assertTrue(character.is_alive())

    def test_is_alive_2(self):
        character = RPGCharacter("John", 0, 20, 10)
        self.assertFalse(character.is_alive())

    def test_is_alive_3(self):
        character = RPGCharacter("John", -10, 20, 10)
        self.assertFalse(character.is_alive())

import unittest

class AgentTest_is_alive(unittest.TestCase):
    def test_is_alive_1(self):
        character = RPGCharacter('player 1', 1, 10, 3)
        self.assertTrue(character.is_alive())

    def test_is_alive_2(self):
        attacker = RPGCharacter('attacker', 100, 10, 3)
        defender = RPGCharacter('defender', 8, 5, 2)
        attacker.attack(defender)
        self.assertEqual(defender.hp, 0)
        self.assertFalse(defender.is_alive())