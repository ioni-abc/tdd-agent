# ClassEval_73

## Skeleton (what the agent sees)

```python
class RPGCharacter:
    """
    The class represents a role-playing game character, which allows to attack other characters, heal, gain experience, level up, and check if the character is alive.
    """

    def __init__(self, name, hp, attack_power, defense, level=1):
        """
        Initialize an RPG character object.
        :param name: strm, the name of the character.
        :param hp: int, The health points of the character.
        :param attack_power: int, the attack power of the character.
        :param defense: int, the defense points of the character.
        :param level: int, the level of the character. Default is 1.
        """
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.defense = defense
        self.level = level
        self.exp = 0

    def attack(self, other_character):
        """
        Attack another character. The damage caused needs to offset the defense value.
        :param other_character: str, The character being attacked.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_2 = RPGCharacter('player 2', 100, 7, 2)
        >>> player_1.attack(player_2)
        >>> player_2.hp
        92
        """

    def heal(self):
        """
        Heal the character with 10 hp and the max hp is 100.
        :return: int, the current health points after healing.
        >>> player_1 = RPGCharacter('player 1', 93, 10, 3)
        >>> player_1.heal()
        100
        """

    def gain_exp(self, amount):
        """
        Gain experience points for the character and level_up when the exp has reached the values that is 100 times the current level
        The experience that overflows should be used to calculate the next leve up untill exhausts
        :param amount: int, the amount of experience points to gain.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.gain_exp(1100)
        >>> player_1.exp
        100
        >>> player_1.level
        5
        """

    def level_up(self):
         """
        Level up the character and return to zero experience points, increase hp by 20 points, attack power and defense points by 5 points.
        max level is 100
        :return: tuple[int, int, int, int], the new level, health points, attack power, and defense points after leveling up.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.level_up()
        (2, 120, 15, 8)
        """

    def is_alive(self):
        """
        Check if player is alive.
        :return: True if the hp is larger than 0, or False otherwise.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.is_alive()
        True
        """
```

## Method `attack`

### Docstring

```python
def attack(self, other_character):
        """
        Attack another character. The damage caused needs to offset the defense value.
        :param other_character: str, The character being attacked.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_2 = RPGCharacter('player 2', 100, 7, 2)
        >>> player_1.attack(player_2)
        >>> player_2.hp
        92
        """
```

### Reference code (`solution_code`)

```python
def attack(self, other_character):
        damage = max(self.attack_power - other_character.defense, 1)
        other_character.hp -= damage
```

### Tests (`RPGCharacterTestAttack`)

**test_attack**: `stated`
- reason: The docstring says damage offsets defense, and its example (attack 10 against defense 2 leaving 92 HP) implies damage = attack power minus defense, which gives the test's expected 85 HP (20 - 5 = 15 damage).

```python
def test_attack(self):
    character1 = RPGCharacter("John", 100, 20, 10)
    character2 = RPGCharacter("Enemy", 100, 15, 5)
    character1.attack(character2)
    self.assertEqual(character2.hp, 85)
```

**test_attack_2**: `stated`
- reason: The docstring's "damage needs to offset the defense value" and its worked example (attack 10 against defense 2 gives 8 damage) imply subtracting defense from attack power, which yields the 5 damage this test expects.

```python
def test_attack_2(self):
    character1 = RPGCharacter("John", 100, 20, 10)
    character2 = RPGCharacter("Enemy", 100, 15, 5)
    character2.attack(character1)
    self.assertEqual(character1.hp, 95)
```

**test_attack_3**: `stated`
- reason: The docstring's example (attack 10 against defense 2 leaves 92 hp) pins down the subtract-defense-from-attack rule that this test exercises with positive damage in both directions.

```python
def test_attack_3(self):
    character1 = RPGCharacter("John", 100, 20, 10)
    character2 = RPGCharacter("Enemy", 100, 15, 5)
    character1.attack(character2)
    character2.attack(character1)
    self.assertEqual(character1.hp, 95)
    self.assertEqual(character2.hp, 85)
```

**test_attack_4**: `stated`
- reason: The docstring says the damage must offset the defense value, and its example (10 attack vs 2 defense takes 100 HP to 92) confirms damage is attack minus defense, so a programmer would implement this test's two repeated attacks as 15 damage each, leaving 70 HP.

```python
def test_attack_4(self):
    character1 = RPGCharacter("John", 100, 20, 10)
    character2 = RPGCharacter("Enemy", 100, 15, 5)
    character1.attack(character2)
    character1.attack(character2)
    self.assertEqual(character2.hp, 70)
```

**test_attack_5**: `stated`
- reason: The docstring's formula (damage is attack minus the defender's defense, subtracted from hp) gives 20 - 5 = 15 per hit, so three hits leave 100 - 45 = 55, which is what the test expects.

```python
def test_attack_5(self):
    character1 = RPGCharacter("John", 100, 20, 10)
    character2 = RPGCharacter("Enemy", 100, 15, 5)
    character1.attack(character2)
    character1.attack(character2)
    character1.attack(character2)
    self.assertEqual(character2.hp, 55)
```

## Method `heal`

### Docstring

```python
def heal(self):
        """
        Heal the character with 10 hp and the max hp is 100.
        :return: int, the current health points after healing.
        >>> player_1 = RPGCharacter('player 1', 93, 10, 3)
        >>> player_1.heal()
        100
        """
```

### Reference code (`solution_code`)

```python
def heal(self):
        self.hp += 10
        if self.hp > 100:
            self.hp = 100
        return self.hp
```

### Tests (`RPGCharacterTestHeal`)

**test_heal_1**: `stated`
- reason: The docstring says heal restores 10 hp with a maximum of 100, so a programmer would implement hp + 10 capped at 100, which yields 100 from 90 as the test expects.

```python
def test_heal_1(self):
    character = RPGCharacter("John", 90, 20, 10)
    character.heal()
    self.assertEqual(character.hp, 100)
```

**test_heal_2**: `stated`
- reason: The docstring says healing adds 10 hp with a maximum of 100, so a programmer would cap 97 + 10 at 100, which is what the test asserts.

```python
def test_heal_2(self):
    character = RPGCharacter("John", 97, 20, 10)
    character.heal()
    self.assertEqual(character.hp, 100)
```

**test_heal_3**: `stated`
- reason: The docstring says heal adds 10 hp and that max hp is 100, so a programmer would cap the result at 100, which gives the expected 100 for an already-full character.

```python
def test_heal_3(self):
    character = RPGCharacter("John", 100, 20, 10)
    character.heal()
    self.assertEqual(character.hp, 100)
```

**test_heal_4**: `stated`
- reason: The docstring says heal restores 10 hp with a cap of 100, so a programmer would add 10 to 50 and get 60, which is what the test asserts.

```python
def test_heal_4(self):
    character = RPGCharacter("John", 100, 20, 10)
    character.hp = 50
    character.heal()
    self.assertEqual(character.hp, 60)
```

**test_heal_5**: `stated`
- reason: The docstring says healing restores 10 hp capped at a max of 100, so a programmer would implement hp += 10 and the test's 10 → 20 expectation follows directly.

```python
def test_heal_5(self):
    character = RPGCharacter("John", 100, 20, 10)
    character.hp = 10
    character.heal()
    self.assertEqual(character.hp, 20)
```

## Method `gain_exp`

### Docstring

```python
def gain_exp(self, amount):
        """
        Gain experience points for the character and level_up when the exp has reached the values that is 100 times the current level
        The experience that overflows should be used to calculate the next leve up untill exhausts
        :param amount: int, the amount of experience points to gain.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.gain_exp(1100)
        >>> player_1.exp
        100
        >>> player_1.level
        5
        """
```

### Reference code (`solution_code`)

```python
def gain_exp(self, amount):
        while amount != 0:
            if self.exp + amount >= self.level * 100:
                amount -= (self.level * 100 - self.exp)
                self.level_up()
            else:
                self.exp += amount
                amount = 0
```

### Tests (`RPGCharacterTestGainExp`)

**test_gain_exp_1**: `stated`
- reason: The docstring specifies that gaining experience equal to the threshold (100 times the current level) triggers a level-up with overflow carried forward, so a programmer following it would produce level 2 and exp 0 from a level-1 character with 0 exp gaining 100.

```python
def test_gain_exp_1(self):
    character = RPGCharacter("John", 100, 20, 10)
    character.gain_exp(100)
    self.assertEqual(character.level, 2)
    self.assertEqual(character.exp, 0)
```

**test_gain_exp_2**: `stated`
- reason: The docstring states the overflow rule (excess experience carries into the next level-up until exhausted) and its example of 1100 exp yielding level 5 with 100 exp, which is the same outcome this test checks.

```python
def test_gain_exp_2(self):
    character = RPGCharacter("John", 100, 20, 10)
    character.gain_exp(1100)
    self.assertEqual(character.level, 5)
    self.assertEqual(character.exp, 100)
```

**test_gain_exp_3**: `stated`
- reason: The docstring says that gaining enough experience levels up at 100 times the current level and that overflow carries into the next level-up, which is exactly what this test checks: 200 points from level 1 gives level 2 with 100 leftover.

```python
def test_gain_exp_3(self):
    character = RPGCharacter("John", 100, 20, 10)
    character.gain_exp(200)
    self.assertEqual(character.level, 2)
    self.assertEqual(character.exp, 100)
```

**test_gain_exp_4**: `unstated`
- reason: The test depends on the character's starting level and exp, which the docstring never specifies; a programmer reading the docstring could assume the fourth constructor argument sets the level, giving level 10 and no level-up from 300 exp, and fail.
- missing: The docstring should state what level and exp a newly constructed character starts with, and which constructor argument sets the level, so the level-up threshold calculation has a known starting point.

```python
def test_gain_exp_4(self):
    character = RPGCharacter("John", 100, 20, 10)
    character.gain_exp(300)
    self.assertEqual(character.level, 3)
    self.assertEqual(character.exp, 0)
```

**test_gain_exp_5**: `stated`
- reason: The docstring describes the rule this test checks: experience overflows past each level-up threshold of 100 times the current level and carries into the next level-up, so a programmer following it would reach level 3 with 100 exp from a starting level of 1.

```python
def test_gain_exp_5(self):
    character = RPGCharacter("John", 100, 20, 10)
    character.gain_exp(400)
    self.assertEqual(character.level, 3)
    self.assertEqual(character.exp, 100)
```

## Method `level_up`

### Docstring

```python
def level_up(self):
         """
        Level up the character and return to zero experience points, increase hp by 20 points, attack power and defense points by 5 points.
        max level is 100
        :return: tuple[int, int, int, int], the new level, health points, attack power, and defense points after leveling up.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.level_up()
        (2, 120, 15, 8)
        """
```

### Reference code (`solution_code`)

```python
def level_up(self):
        if self.level < 100:
            self.level += 1
            self.exp = 0
            self.hp += 20
            self.attack_power += 5
            self.defense += 5
        return self.level, self.hp, self.attack_power, self.defense
```

### Tests (`RPGCharacterTestLevelUp`)

**test_level_up_1**: `stated`
- reason: The docstring states that leveling up increases level by one, resets experience to zero, adds 20 to hp, and adds 5 to attack power and defense, which is exactly what the test checks.

```python
def test_level_up_1(self):
    character = RPGCharacter("John", 100, 20, 10)
    character.level_up()
    self.assertEqual(character.level, 2)
    self.assertEqual(character.exp, 0)
    self.assertEqual(character.hp, 120)
    self.assertEqual(character.attack_power, 25)
    self.assertEqual(character.defense, 15)
```

**test_level_up_2**: `stated`
- reason: The docstring says the max level is 100, so a programmer would implement level_up as a no-op at level 100, leaving the level, hp, attack power and defense unchanged, which is what the test asserts.

```python
def test_level_up_2(self):
    character = RPGCharacter("John", 100, 20, 10, 100)
    character.level_up()
    self.assertEqual(character.level, 100)
    self.assertEqual(character.exp, 0)
    self.assertEqual(character.hp, 100)
    self.assertEqual(character.attack_power, 20)
    self.assertEqual(character.defense, 10)
```

**test_level_up_3**: `stated`
- reason: The docstring says leveling up resets experience to zero, adds 20 hp, and adds 5 to attack power and defense, which is exactly what the test checks for a character starting at level 2.

```python
def test_level_up_3(self):
    character = RPGCharacter("John", 100, 20, 10, 2)
    character.level_up()
    self.assertEqual(character.level, 3)
    self.assertEqual(character.exp, 0)
    self.assertEqual(character.hp, 120)
    self.assertEqual(character.attack_power, 25)
    self.assertEqual(character.defense, 15)
```

**test_level_up_4**: `stated`
- reason: The docstring says leveling up returns experience to zero, adds 20 HP, and adds 5 to attack power and defense, and the test's level 3 to 4, exp 0, HP 100 to 120, attack 20 to 25, and defense 10 to 15 follow directly from those rules.

```python
def test_level_up_4(self):
    character = RPGCharacter("John", 100, 20, 10, 3)
    character.level_up()
    self.assertEqual(character.level, 4)
    self.assertEqual(character.exp, 0)
    self.assertEqual(character.hp, 120)
    self.assertEqual(character.attack_power, 25)
    self.assertEqual(character.defense, 15)
```

**test_level_up_5**: `stated`
- reason: The docstring says leveling up resets experience to zero, adds 20 hp, and adds 5 to attack power and defense, which is exactly what the test checks, and the level increment is implied by "level up".

```python
def test_level_up_5(self):
    character = RPGCharacter("John", 100, 20, 10, 4)
    character.level_up()
    self.assertEqual(character.level, 5)
    self.assertEqual(character.exp, 0)
    self.assertEqual(character.hp, 120)
    self.assertEqual(character.attack_power, 25)
    self.assertEqual(character.defense, 15)
```

## Method `is_alive`

### Docstring

```python
def is_alive(self):
        """
        Check if player is alive.
        :return: True if the hp is larger than 0, or False otherwise.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.is_alive()
        True
        """
```

### Reference code (`solution_code`)

```python
def is_alive(self):
        return self.hp > 0
```

### Tests (`RPGCharacterTestIsAlive`)

**test_is_alive_1**: `stated`
- reason: The docstring says is_alive returns True when hp is greater than 0, and the test creates a character with positive hp (100) and asserts True, which a programmer following the docstring would pass.

```python
def test_is_alive_1(self):
    character = RPGCharacter("John", 100, 20, 10)
    self.assertTrue(character.is_alive())
```

**test_is_alive_2**: `stated`
- reason: The docstring says is_alive returns True only when hp is larger than 0 and False otherwise, so a hp of 0 must yield False, which is what the test checks.

```python
def test_is_alive_2(self):
    character = RPGCharacter("John", 0, 20, 10)
    self.assertFalse(character.is_alive())
```

**test_is_alive_3**: `stated`
- reason: The docstring says the method returns True only when hp is larger than 0 and False otherwise, so a negative hp must return False, which is what the test checks.

```python
def test_is_alive_3(self):
    character = RPGCharacter("John", -10, 20, 10)
    self.assertFalse(character.is_alive())
```

**test_is_alive_4**: `stated`
- reason: The docstring says is_alive returns True when hp is larger than 0, so a programmer would return True for an hp of 1, which is what the test expects.

```python
def test_is_alive_4(self):
    character = RPGCharacter("John", 1, 20, 10)
    self.assertTrue(character.is_alive())
```

**test_is_alive_5**: `stated`
- reason: The docstring says is_alive returns True when hp is larger than 0, and the test creates a character with hp 10 and asserts True, which a programmer following the docstring would pass.

```python
def test_is_alive_5(self):
    character = RPGCharacter("John", 10, 20, 10)
    self.assertTrue(character.is_alive())
```

## Tests in no method's test class

### `RPGCharacterTestMain`

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    character1 = RPGCharacter("John", 100, 20, 10)
    character2 = RPGCharacter("Enemy", 100, 15, 5)
    character1.attack(character2)
    self.assertEqual(character2.hp, 85)
    character2.heal()
    self.assertEqual(character2.hp, 95)
    character1.gain_exp(200)
    self.assertEqual(character1.exp, 100)
    self.assertEqual(character1.hp, 120)
    self.assertEqual(character1.attack_power, 25)
    self.assertEqual(character1.defense, 15)
    self.assertTrue(character1.is_alive())
```
