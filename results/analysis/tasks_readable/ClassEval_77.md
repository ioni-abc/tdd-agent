# ClassEval_77

## Skeleton (what the agent sees)

```python
import random

class Snake:
    """
    The class is a snake game, with allows snake to move and eat food, and also enables to reset, and generat a random food position.
    """

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, BLOCK_SIZE, food_position):
        """
        Initialize the length of the snake, screen width, screen height, block size, snake head position, score, and food position.
        :param SCREEN_WIDTH: int
        :param SCREEN_HEIGHT: int
        :param BLOCK_SIZE: int, Size of moving units
        :param food_position: tuple, representing the position(x, y) of food.
        """
        self.length = 1
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.BLOCK_SIZE = BLOCK_SIZE
        self.positions = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
        self.score = 0
        self.food_position = food_position


    def move(self, direction):
        """
        Move the snake in the specified direction. If the new position of the snake's head is equal to the position of the food, then eat the food; If the position of the snake's head is equal to the position of its body, then start over, otherwise its own length plus one.
        :param direction: tuple, representing the direction of movement (x, y).
        :return: None
        >>> snake.move((1,1))
        self.length = 1
        self.positions = [(51, 51), (50, 50)]
        self.score = 10
        """


    def random_food_position(self):
        """
        Randomly generate a new food position, but don't place it on the snake.
        :return: None, Change the food position
        """


    def reset(self):
        """
        Reset the snake to its initial state. Set the length to 1, the snake head position to ((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2)), the score to 0, and randomly generate new food position.
        :return: None
        >>> snake = Snake(100, 100, 1, (51, 51))
        >>> snake.reset()
        self.length = 1
        self.positions = [(50, 50)]
        self.score = 0
        self.random_food_position()
        """


    def eat_food(self):
        """
        Increase the length of the snake by 1 and increase the score by 100. Randomly generate a new food position, but
        don't place it on the snake.
        :return: None
        >>> snake = Snake(100, 100, 1, (51, 51))
        >>> snake.move((1,1))
        >>> snake.eat_food()
        self.length = 2
        self.score = 10
        """
```

## Method `move`

### Docstring

```python
def move(self, direction):
        """
        Move the snake in the specified direction. If the new position of the snake's head is equal to the position of the food, then eat the food; If the position of the snake's head is equal to the position of its body, then start over, otherwise its own length plus one.
        :param direction: tuple, representing the direction of movement (x, y).
        :return: None
        >>> snake.move((1,1))
        self.length = 1
        self.positions = [(51, 51), (50, 50)]
        self.score = 10
        """
```

### Reference code (`solution_code`)

```python
def move(self, direction):
        cur = self.positions[0]
        x, y = direction

        new = (
            ((cur[0] + (x * self.BLOCK_SIZE)) % self.SCREEN_WIDTH),
            (cur[1] + (y * self.BLOCK_SIZE)) % self.SCREEN_HEIGHT,
        )

        if new == self.food_position:
            self.eat_food()

        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
```

### Tests (`SnakeTestMove`)

**test_move_1**: `contradicts`
- reason: The docstring's example shows the snake keeping length 1 and score 10 after moving onto the food, while the test and reference code expect length 2 and score 100 after eating.
- missing: The docstring should state the exact score gained when the snake eats food and how its length changes, and its example output should match that rule.

```python
def test_move_1(self):
    snake = Snake(100, 100, 1, (51, 51))
    snake.move((1, 1))
    self.assertEqual(snake.length, 2)
    self.assertEqual(snake.positions[0], (51, 51))
    self.assertEqual(snake.positions[1], (50, 50))
    self.assertEqual(snake.score, 100)
```

**test_move_2**: `contradicts`
- reason: The docstring's example shows `self.score = 10` after the move, while the test expects `snake.score` to remain 0 because the head does not reach the food.
- missing: The docstring should state that the score changes only when the head lands on the food, stay unchanged otherwise, and that the example values must match the stated snake length and positions.

```python
def test_move_2(self):
    snake = Snake(100, 100, 1, (80, 80))
    snake.move((1, 1))
    self.assertEqual(snake.length, 1)
    self.assertEqual(snake.positions[0], (51, 51))
    self.assertEqual(snake.score, 0)
```

**test_move_3**: `unstated`
- reason: The test expects the head to land at (51, 50) after moving in direction (1, 0), but the docstring never says how a direction tuple maps to coordinate changes, so a programmer following it could reasonably produce a different position.
- missing: The docstring should state the exact coordinate change for a given direction tuple (the step size per unit of direction, and whether the y-axis increases or decreases), including how the head position is computed from the current head and the direction.

```python
def test_move_3(self):
    snake = Snake(100, 100, 1, (51, 51))
    snake.move((1, 0))
    self.assertEqual(snake.length, 1)
    self.assertEqual(snake.positions[0], (51, 50))
    self.assertEqual(snake.score, 0)
```

**test_move_4**: `unstated`
- reason: The test expects a zero-direction move to leave the head at its starting position with length 1 and score 0, but the docstring never says how a zero or null direction is handled or where the head starts.
- missing: The docstring should say that the new head is the current head plus the direction scaled by block size, with wrap-around at screen edges, and state what happens when the direction is (0, 0) (the head stays put and the length and score are unchanged).

```python
def test_move_4(self):
    snake = Snake(100, 100, 1, (51, 51))
    snake.move((0, 0))
    self.assertEqual(snake.length, 1)
    self.assertEqual(snake.positions[0], (50, 50))
    self.assertEqual(snake.score, 0)
```

**test_move_5**: `unstated`
- reason: The test expects the head to shift by the direction scaled by block size, with no food eaten and the length and score unchanged, but the docstring never says the head moves by that step or that the length stays fixed, and its "its own length plus one" phrase is too garbled to clearly state either.
- missing: The docstring should state that the head moves one block size times the direction vector (wrapping around the screen edges), that the snake's length only grows when it eats food, and that the score is unchanged when no food is eaten.

```python
def test_move_5(self):
    snake = Snake(100, 100, 1, (99, 99))
    snake.move((1, 0))
    self.assertEqual(snake.length, 1)
    self.assertEqual(snake.positions[0], (51, 50))
    self.assertEqual(snake.score, 0)
```

## Method `random_food_position`

### Docstring

```python
def random_food_position(self):
        """
        Randomly generate a new food position, but don't place it on the snake.
        :return: None, Change the food position
        """
```

### Reference code (`solution_code`)

```python
def random_food_position(self):
        while self.food_position in self.positions:
            self.food_position = (random.randint(0, self.SCREEN_WIDTH // self.BLOCK_SIZE - 1) * self.BLOCK_SIZE,
                                  random.randint(0, self.SCREEN_HEIGHT // self.BLOCK_SIZE - 1) * self.BLOCK_SIZE)
```

### Tests (`SnakeTestRandomFoodPosition`)

**test_random_food_position_1**: `unstated`
- reason: The test's core check, that the new food is not on the snake, matches the docstring, but it also requires the food to lie within the screen bounds (0 to 100), which the docstring never mentions.
- missing: The docstring should state that the new food position must be a grid-aligned coordinate inside the screen area, so that a random position anywhere in the screen's block grid is valid, in addition to not overlapping the snake.

```python
def test_random_food_position_1(self):
    snake = Snake(100, 100, 1, (51, 51))
    self.assertEqual(snake.food_position, (51, 51))
    snake.random_food_position()
    self.assertNotIn(snake.food_position, snake.positions)
    self.assertGreaterEqual(snake.food_position[0], 0)
    self.assertGreaterEqual(snake.food_position[1], 0)
    self.assertLessEqual(snake.food_position[0], 100)
    self.assertLessEqual(snake.food_position[1], 100)
```

**test_random_food_position_2**: `unstated`
- reason: The docstring requires only that the new food avoid the snake, but the test also requires the food's coordinates to fall within the screen bounds, which the docstring never mentions, so a correct implementation could place food outside that range and fail.
- missing: The docstring should state that the new food position must lie inside the playing area, with each coordinate between 0 and the screen size minus one block, on block-size multiples.

```python
def test_random_food_position_2(self):
    snake = Snake(100, 100, 1, (99, 99))
    self.assertEqual(snake.food_position, (99, 99))
    snake.random_food_position()
    self.assertNotIn(snake.food_position, snake.positions)
    self.assertGreaterEqual(snake.food_position[0], 0)
    self.assertGreaterEqual(snake.food_position[1], 0)
    self.assertLessEqual(snake.food_position[0], 100)
    self.assertLessEqual(snake.food_position[1], 100)
```

**test_random_food_position_3**: `unstated`
- reason: The docstring only says the food must avoid the snake, but the test also requires the coordinates to fall within a bounded range, so a correct implementation that picks positions outside the screen could fail.
- missing: The docstring should state that the new food position must lie inside the screen area and be aligned to the block grid (multiples of the block size), with no coordinate outside the playfield.

```python
def test_random_food_position_3(self):
    snake = Snake(100, 100, 1, (0, 0))
    self.assertEqual(snake.food_position, (0, 0))
    snake.random_food_position()
    self.assertNotIn(snake.food_position, snake.positions)
    self.assertGreaterEqual(snake.food_position[0], 0)
    self.assertGreaterEqual(snake.food_position[1], 0)
    self.assertLessEqual(snake.food_position[0], 100)
    self.assertLessEqual(snake.food_position[1], 100)
```

**test_random_food_position_4**: `unstated`
- reason: The docstring says the new food must not land on the snake, which the test checks, but it does not say the food must stay within the screen bounds, which the test also asserts.
- missing: The docstring should state that the new food coordinates must lie on the play grid, within the screen's width and height, and be aligned to the grid's block size.

```python
def test_random_food_position_4(self):
    snake = Snake(100, 100, 1, (40, 40))
    self.assertEqual(snake.food_position, (40, 40))
    snake.random_food_position()
    self.assertNotIn(snake.food_position, snake.positions)
    self.assertGreaterEqual(snake.food_position[0], 0)
    self.assertGreaterEqual(snake.food_position[1], 0)
    self.assertLessEqual(snake.food_position[0], 100)
    self.assertLessEqual(snake.food_position[1], 100)
```

**test_random_food_position_5**: `unstated`
- reason: The docstring states that the food must not land on the snake, which the test checks, but it does not say the food must fall inside the screen bounds, which the test also asserts.
- missing: The docstring should state that the new food position must lie within the screen area and be aligned to the block grid (multiples of the block size, from zero up to the screen size minus one block), in addition to avoiding the snake's body.

```python
def test_random_food_position_5(self):
    snake = Snake(100, 100, 1, (60, 60))
    self.assertEqual(snake.food_position, (60, 60))
    snake.random_food_position()
    self.assertNotIn(snake.food_position, snake.positions)
    self.assertGreaterEqual(snake.food_position[0], 0)
    self.assertGreaterEqual(snake.food_position[1], 0)
    self.assertLessEqual(snake.food_position[0], 100)
    self.assertLessEqual(snake.food_position[1], 100)
```

## Method `reset`

### Docstring

```python
def reset(self):
        """
        Reset the snake to its initial state. Set the length to 1, the snake head position to ((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2)), the score to 0, and randomly generate new food position.
        :return: None
        >>> snake = Snake(100, 100, 1, (51, 51))
        >>> snake.reset()
        self.length = 1
        self.positions = [(50, 50)]
        self.score = 0
        self.random_food_position()
        """
```

### Reference code (`solution_code`)

```python
def reset(self):
        self.length = 1
        self.positions = [((self.SCREEN_WIDTH / 2), (self.SCREEN_HEIGHT / 2))]
        self.score = 0
        self.random_food_position()
```

### Tests (`SnakeTestReset`)

**test_reset_1**: `stated`
- reason: The docstring says reset sets length to 1, the head to (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), and score to 0, which with a 100x100 screen gives the (50, 50) head position and the length and score values the test checks.

```python
def test_reset_1(self):
    snake = Snake(100, 100, 1, (51, 51))
    snake.move((1, 1))
    snake.reset()
    self.assertEqual(snake.length, 1)
    self.assertEqual(snake.positions[0], (50, 50))
    self.assertEqual(snake.score, 0)
```

**test_reset_2**: `stated`
- reason: The docstring specifies that reset sets length to 1, the head to half the screen width and height (which is (50, 50) for a 100x100 screen), and the score to 0, so a programmer following it would pass these assertions.

```python
def test_reset_2(self):
    snake = Snake(100, 100, 1, (51, 51))
    snake.move((0, 1))
    snake.reset()
    self.assertEqual(snake.length, 1)
    self.assertEqual(snake.positions[0], (50, 50))
    self.assertEqual(snake.score, 0)
```

**test_reset_3**: `stated`
- reason: The docstring says reset sets length to 1, the head to (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), and score to 0, which for a 100x100 screen gives the (50, 50) and length/score values the test checks.

```python
def test_reset_3(self):
    snake = Snake(100, 100, 1, (51, 51))
    snake.move((0, -1))
    snake.reset()
    self.assertEqual(snake.length, 1)
    self.assertEqual(snake.positions[0], (50, 50))
    self.assertEqual(snake.score, 0)
```

**test_reset_4**: `stated`
- reason: The docstring specifies that reset sets length to 1, the head to the screen-centre position (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), and the score to 0, which is exactly what the test checks after a move.

```python
def test_reset_4(self):
    snake = Snake(100, 100, 1, (51, 51))
    snake.move((-1, 0))
    snake.reset()
    self.assertEqual(snake.length, 1)
    self.assertEqual(snake.positions[0], (50, 50))
    self.assertEqual(snake.score, 0)
```

**test_reset_5**: `stated`
- reason: The docstring says reset sets length to 1, the head to the screen centre (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), and score to 0, which is exactly what this test checks after a move.

```python
def test_reset_5(self):
    snake = Snake(100, 100, 1, (51, 51))
    snake.move((1, 0))
    snake.reset()
    self.assertEqual(snake.length, 1)
    self.assertEqual(snake.positions[0], (50, 50))
    self.assertEqual(snake.score, 0)
```

## Method `eat_food`

### Docstring

```python
def eat_food(self):
        """
        Increase the length of the snake by 1 and increase the score by 100. Randomly generate a new food position, but
        don't place it on the snake.
        :return: None
        >>> snake = Snake(100, 100, 1, (51, 51))
        >>> snake.move((1,1))
        >>> snake.eat_food()
        self.length = 2
        self.score = 10
        """
```

### Reference code (`solution_code`)

```python
def eat_food(self):
        self.length += 1
        self.score += 100
        self.random_food_position()
```

### Tests (`SnakeTestEatFood`)

**test_eat_food_1**: `stated`
- reason: The docstring says eat_food increases length by 1 and score by 100, which is exactly what the test checks (length 1 to 2, score 0 to 100), though its doctest example wrongly shows score 10.

```python
def test_eat_food_1(self):
    snake = Snake(100, 100, 1, (51, 51))
    self.assertEqual(snake.length, 1)
    self.assertEqual(snake.score, 0)
    snake.eat_food()
    self.assertEqual(snake.length, 2)
    self.assertEqual(snake.score, 100)
```

**test_eat_food_2**: `stated`
- reason: The docstring says each call increases the length by 1 and the score by 100, so a programmer following it would get length 3 and score 200 after two calls starting from length 1 and score 0, which is what the test checks.

```python
def test_eat_food_2(self):
    snake = Snake(100, 100, 1, (51, 51))
    self.assertEqual(snake.length, 1)
    self.assertEqual(snake.score, 0)
    snake.eat_food()
    snake.eat_food()
    self.assertEqual(snake.length, 3)
    self.assertEqual(snake.score, 200)
```

**test_eat_food_3**: `stated`
- reason: The docstring says each call adds 1 to the length and 100 to the score, so a programmer following it would get length 4 and score 300 after three calls from length 1 and score 0.

```python
def test_eat_food_3(self):
    snake = Snake(100, 100, 1, (51, 51))
    self.assertEqual(snake.length, 1)
    self.assertEqual(snake.score, 0)
    snake.eat_food()
    snake.eat_food()
    snake.eat_food()
    self.assertEqual(snake.length, 4)
    self.assertEqual(snake.score, 300)
```

**test_eat_food_4**: `stated`
- reason: The docstring says each call increases length by 1 and score by 100, which is exactly what four calls from length 1 and score 0 should produce (length 5, score 400).

```python
def test_eat_food_4(self):
    snake = Snake(100, 100, 1, (51, 51))
    self.assertEqual(snake.length, 1)
    self.assertEqual(snake.score, 0)
    snake.eat_food()
    snake.eat_food()
    snake.eat_food()
    snake.eat_food()
    self.assertEqual(snake.length, 5)
    self.assertEqual(snake.score, 400)
```

**test_eat_food_5**: `stated`
- reason: The docstring says each call adds 1 to the length and 100 to the score, so five calls from length 1 and score 0 give length 6 and score 500, which is what the test checks.

```python
def test_eat_food_5(self):
    snake = Snake(100, 100, 1, (51, 51))
    self.assertEqual(snake.length, 1)
    self.assertEqual(snake.score, 0)
    snake.eat_food()
    snake.eat_food()
    snake.eat_food()
    snake.eat_food()
    snake.eat_food()
    self.assertEqual(snake.length, 6)
    self.assertEqual(snake.score, 500)
```

## Tests in no method's test class

### `SnakeTest`

**test_snake**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_snake(self):
    snake = Snake(100, 100, 1, (51, 51))
    self.assertEqual(snake.length, 1)
    self.assertEqual(snake.SCREEN_WIDTH, 100)
    self.assertEqual(snake.SCREEN_HEIGHT, 100)
    self.assertEqual(snake.BLOCK_SIZE, 1)
    self.assertEqual(snake.positions[0], (50, 50))
    self.assertEqual(snake.score, 0)
    self.assertEqual(snake.food_position, (51, 51))
    snake.move((1, 1))
    self.assertEqual(snake.length, 2)
    self.assertEqual(snake.positions[0], (51, 51))
    self.assertEqual(snake.score, 100)
    snake.random_food_position()
    self.assertNotIn(snake.food_position, snake.positions)
    snake.reset()
    self.assertEqual(snake.length, 1)
    self.assertEqual(snake.positions[0], (50, 50))
    self.assertEqual(snake.score, 0)
```
