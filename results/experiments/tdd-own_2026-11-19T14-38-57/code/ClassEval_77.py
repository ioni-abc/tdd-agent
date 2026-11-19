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
        head = self.positions[0]
        dx, dy = direction
        new_head = (head[0] + dx * self.BLOCK_SIZE, head[1] + dy * self.BLOCK_SIZE)

        # Collided with its own body: start over.
        if new_head in self.positions:
            self.reset()
            return None

        self.positions.insert(0, new_head)

        # Ate the food: grow and place new food.
        if new_head == tuple(self.food_position):
            self.eat_food()

        # Keep only as many segments as the snake's length.
        del self.positions[self.length:]
        return None


    def random_food_position(self):
        """
        Randomly generate a new food position, but don't place it on the snake.
        :return: None, Change the food position
        """
        xs = list(range(0, int(self.SCREEN_WIDTH), int(self.BLOCK_SIZE)))
        ys = list(range(0, int(self.SCREEN_HEIGHT), int(self.BLOCK_SIZE)))
        if not xs or not ys:
            return None

        total_cells = len(xs) * len(ys)
        if len(self.positions) >= total_cells:
            # No free cell is available; nothing sensible to place.
            return None

        # Fast path: rejection sampling.
        for _ in range(100):
            candidate = (random.choice(xs), random.choice(ys))
            if candidate not in self.positions:
                self.food_position = candidate
                return None

        # Fallback: collect all free cells and pick one at random.
        free_cells = [
            (x, y)
            for x in xs
            for y in ys
            if (x, y) not in self.positions
        ]
        self.food_position = random.choice(free_cells)
        return None


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
        self.length = 1
        self.positions = [((self.SCREEN_WIDTH / 2), (self.SCREEN_HEIGHT / 2))]
        self.score = 0
        self.random_food_position()
        return None


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
        self.length += 1
        self.score += 100
        self.random_food_position()
        return None