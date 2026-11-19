import unittest


import unittest

class AgentTest_attack(unittest.TestCase):

    def test_attack_1(self):
        # Spec example: attack 10 vs defense 2 deals 8 damage, 100 -> 92 hp.
        player_1 = RPGCharacter('player 1', 100, 10, 3)
        player_2 = RPGCharacter('player 2', 100, 7, 2)
        player_1.attack(player_2)
        self.assertEqual(player_2.hp, 92)

    def test_attack_2(self):
        # Damage is attack power minus the defender's defense (10 - 3 = 7).
        attacker = RPGCharacter('attacker', 100, 10, 3)
        defender = RPGCharacter('defender', 100, 7, 3)
        attacker.attack(defender)
        self.assertEqual(defender.hp, 93)

    def test_attack_3(self):
        # Attacking another character should not change the attacker's hp.
        attacker = RPGCharacter('attacker', 100, 10, 3)
        defender = RPGCharacter('defender', 100, 7, 2)
        attacker.attack(defender)
        self.assertEqual(attacker.hp, 100)

    def test_attack_4(self):
        # Repeated attacks accumulate damage: two hits of 8 damage each.
        attacker = RPGCharacter('attacker', 100, 10, 3)
        defender = RPGCharacter('defender', 100, 7, 2)
        attacker.attack(defender)
        attacker.attack(defender)
        self.assertEqual(defender.hp, 84)

    def test_attack_5(self):
        # Attacking should not alter the attacker's or the defender's stats
        # other than the defender's hp.
        attacker = RPGCharacter('attacker', 100, 10, 3)
        defender = RPGCharacter('defender', 100, 7, 2)
        attacker.attack(defender)
        self.assertEqual(attacker.attack_power, 10)
        self.assertEqual(attacker.defense, 3)
        self.assertEqual(defender.attack_power, 7)
        self.assertEqual(defender.defense, 2)

import unittest

class AgentTest_heal(unittest.TestCase):

    def test_heal_1(self):
        # Spec example: 93 hp healed by 10 is capped at the max of 100.
        player_1 = RPGCharacter('player 1', 93, 10, 3)
        result = player_1.heal()
        self.assertEqual(result, 100)
        self.assertEqual(player_1.hp, 100)

    def test_heal_2(self):
        # Healing restores 10 hp when the result stays below the max of 100.
        player_1 = RPGCharacter('player 1', 50, 10, 3)
        result = player_1.heal()
        self.assertEqual(result, 60)
        self.assertEqual(player_1.hp, 60)

    def test_heal_3(self):
        # A character already at max hp stays at 100 and heal returns 100.
        player_1 = RPGCharacter('player 1', 100, 10, 3)
        result = player_1.heal()
        self.assertEqual(result, 100)
        self.assertEqual(player_1.hp, 100)

    def test_heal_4(self):
        # Healing 95 hp must be capped at 100, not raised to 105.
        player_1 = RPGCharacter('player 1', 95, 10, 3)
        result = player_1.heal()
        self.assertEqual(result, 100)
        self.assertEqual(player_1.hp, 100)

    def test_heal_5(self):
        # Repeated healing adds 10 each time until the max of 100 is reached.
        player_1 = RPGCharacter('player 1', 80, 10, 3)
        self.assertEqual(player_1.heal(), 90)
        self.assertEqual(player_1.heal(), 100)
        self.assertEqual(player_1.heal(), 100)
        self.assertEqual(player_1.hp, 100)

import unittest

class AgentTest_level_up(unittest.TestCase):

    def test_level_up_1(self):
        # Spec example: a level 1 character with 100 hp, 10 attack, 3 defense
        # levels up to (2, 120, 15, 8).
        player_1 = RPGCharacter('player 1', 100, 10, 3)
        result = player_1.level_up()
        self.assertEqual(result, (2, 120, 15, 8))

    def test_level_up_2(self):
        # Leveling up increases the level by 1 and updates the character's
        # attributes to match the returned values.
        player_1 = RPGCharacter('player 1', 100, 10, 3)
        player_1.level_up()
        self.assertEqual(player_1.level, 2)
        self.assertEqual(player_1.hp, 120)
        self.assertEqual(player_1.attack_power, 15)
        self.assertEqual(player_1.defense, 8)

    def test_level_up_3(self):
        # The increases are fixed: hp +20, attack power +5, defense +5,
        # regardless of the starting level. A level 3 character becomes level 4.
        player_1 = RPGCharacter('player 1', 150, 20, 12, level=3)
        result = player_1.level_up()
        self.assertEqual(result, (4, 170, 25, 17))

    def test_level_up_4(self):
        # Leveling up returns the character to zero experience points.
        player_1 = RPGCharacter('player 1', 100, 10, 3)
        player_1.exp = 50
        player_1.level_up()
        self.assertEqual(player_1.exp, 0)

    def test_level_up_5(self):
        # The maximum level is 100, so a character already at level 100
        # cannot level up further and remains at level 100.
        player_1 = RPGCharacter('player 1', 100, 10, 3, level=100)
        result = player_1.level_up()
        self.assertEqual(result[0], 100)
        self.assertEqual(player_1.level, 100)

import unittest

class AgentTest_gain_exp(unittest.TestCase):

    def test_gain_exp_1(self):
        # Spec example: gaining 1100 exp from level 1 overflows through levels 1-4
        # (100 + 200 + 300 + 400 = 1000 used), leaving 100 exp at level 5.
        player_1 = RPGCharacter('player 1', 100, 10, 3)
        player_1.gain_exp(1100)
        self.assertEqual(player_1.exp, 100)
        self.assertEqual(player_1.level, 5)

    def test_gain_exp_2(self):
        # Gaining less than the 100 exp needed for level 2 adds exp without leveling up.
        player_1 = RPGCharacter('player 1', 100, 10, 3)
        player_1.gain_exp(50)
        self.assertEqual(player_1.exp, 50)
        self.assertEqual(player_1.level, 1)

    def test_gain_exp_3(self):
        # Gaining exactly the threshold (100 exp at level 1) levels up once
        # and leaves zero experience.
        player_1 = RPGCharacter('player 1', 100, 10, 3)
        player_1.gain_exp(100)
        self.assertEqual(player_1.level, 2)
        self.assertEqual(player_1.exp, 0)

    def test_gain_exp_4(self):
        # Reaching the level-up threshold applies the level-up stat increases:
        # hp +20, attack power +5, defense +5.
        player_1 = RPGCharacter('player 1', 100, 10, 3)
        player_1.gain_exp(100)
        self.assertEqual(player_1.hp, 120)
        self.assertEqual(player_1.attack_power, 15)
        self.assertEqual(player_1.defense, 8)

    def test_gain_exp_5(self):
        # A level 2 character needs 200 exp to reach level 3. Gaining 250 exp
        # levels up once, and the 50 overflow exp remains.
        player_1 = RPGCharacter('player 1', 100, 10, 3, level=2)
        player_1.gain_exp(250)
        self.assertEqual(player_1.level, 3)
        self.assertEqual(player_1.exp, 50)

class AgentTest_is_alive(unittest.TestCase):

    def test_is_alive_1(self):
        # Spec example: a character with 100 hp is alive.
        player_1 = RPGCharacter('player 1', 100, 10, 3)
        self.assertIs(player_1.is_alive(), True)

    def test_is_alive_2(self):
        # Boundary: hp of exactly 1 is larger than 0, so the character is alive.
        player_1 = RPGCharacter('player 1', 1, 10, 3)
        self.assertIs(player_1.is_alive(), True)

    def test_is_alive_3(self):
        # Boundary: hp of exactly 0 is not larger than 0, so the character is not alive.
        player_1 = RPGCharacter('player 1', 0, 10, 3)
        self.assertIs(player_1.is_alive(), False)

    def test_is_alive_4(self):
        # Negative hp is not larger than 0, so the character is not alive.
        player_1 = RPGCharacter('player 1', -5, 10, 3)
        self.assertIs(player_1.is_alive(), False)

    def test_is_alive_5(self):
        # Damage reducing hp to exactly 0 makes the character not alive.
        # Attack 10 against defense 2 deals 8 damage, so 8 hp drops to 0.
        attacker = RPGCharacter('attacker', 100, 10, 3)
        defender = RPGCharacter('defender', 8, 7, 2)
        attacker.attack(defender)
        self.assertIs(defender.is_alive(), False)