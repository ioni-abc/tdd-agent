# ClassEval_35

## Skeleton (what the agent sees)

```python
class EightPuzzle:
    """
    This class is an implementation of the classic 8-puzzle game, including methods for finding the blank tile, making moves, getting possible moves, and solving the puzzle using a breadth-first search algorithm.
    """

    def __init__(self, initial_state):
        """
        Initializing the initial state of Eight Puzzle Game, stores in attribute self.initial_state.
        And set the goal state of this game, stores in self.goal_state. In this case, set the size as 3*3
        :param initial_state: a 3*3 size list of Integer, stores the initial state
        """
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def find_blank(self, state):
        """
        Find the blank position of current state, which is the 0 element.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return i, j: two Integers, represent the coordinate of the blank block.
        >>> eightPuzzle = EightPuzzle([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        >>> eightPuzzle.find_blank([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        (2, 1)
        """

    def move(self, state, direction):
        """
        Find the blank block, then makes the board moves forward the given direction.
        :param state: a 3*3 size list of Integer, stores the state before moving.
        :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        >>> eightPuzzle.move([[2, 3, 4], [5, 8, 1], [6, 0, 7]], 'left')
        [[2, 3, 4], [5, 8, 1], [0, 6, 7]]
        """

    def get_possible_moves(self, state):
        """
        According the current state, find all the possible moving directions. Only has 4 direction 'up', 'down', 'left', 'right'.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return moves: a list of str, store all the possible moving directions according to the current state.
        >>> eightPuzzle.get_possible_moves([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        ['up', 'left', 'right']
        """

    def solve(self):
        """
        Use BFS algorithm to find the path solution which makes the initial state to the goal method.
        Maintain a list as a queue, named as open_list, append the initial state.
        Always visit and pop the 0 index element, invoke get_possible_moves method find all the possible directions.
        Traversal the possible_moves list and invoke move method to get several new states.Then append them.
        redo the above steps until the open_list is empty or the state has changed to the goal state.
        :return path: list of str, the solution to the goal state.
        >>> eightPuzzle = EightPuzzle([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
        >>> eightPuzzle.solve()
        ['right']
        """
```

## Method `find_blank`

### Docstring

```python
def find_blank(self, state):
        """
        Find the blank position of current state, which is the 0 element.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return i, j: two Integers, represent the coordinate of the blank block.
        >>> eightPuzzle = EightPuzzle([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        >>> eightPuzzle.find_blank([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        (2, 1)
        """
```

### Reference code (`solution_code`)

```python
def find_blank(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j
```

### Tests (`EightPuzzleTestFindBlank`)

**test_find_blank_1**: `stated`
- reason: The docstring says the method returns the (row, column) coordinate of the 0 element and gives an example whose answer is (2, 1), which matches what the test checks.

```python
def test_find_blank_1(self):
    state = [[2, 3, 4], [5, 8, 1], [6, 0, 7]]
    eightPuzzle = EightPuzzle(state)
    self.assertEqual(eightPuzzle.find_blank(state), (2, 1))
```

**test_find_blank_2**: `stated`
- reason: The docstring says to find the 0 element and return its coordinates as (row, column), and its example confirms that indexing, so a programmer following it would return (1, 1) for the 0 at the centre of the grid.

```python
def test_find_blank_2(self):
    state = [[2, 3, 4], [5, 0, 1], [6, 8, 7]]
    eightPuzzle = EightPuzzle(state)
    self.assertEqual(eightPuzzle.find_blank(state), (1, 1))
```

**test_find_blank_3**: `unstated`
- reason: The docstring defines the blank as the 0 element and says it returns coordinates, but it never says what happens when the grid has no 0, which is the case this test checks (expecting None).
- missing: The docstring should specify the return value when the state contains no 0 element, such as returning None or raising an error.

```python
def test_find_blank_3(self):
    state = [[2, 3, 4], [5, 8, 1], [6, 8, 7]]
    eightPuzzle = EightPuzzle(state)
    self.assertEqual(eightPuzzle.find_blank(state), None)
```

**test_find_blank_4**: `unstated`
- reason: The docstring says to return the coordinates of the 0 block, but it never says what to return when no 0 is present, and this test expects `None` for a state with no 0.
- missing: The docstring should state the return value when the state contains no 0 element (for example, that it returns `None`).

```python
def test_find_blank_4(self):
    state = [[2, 3, 4], [5, 8, 1], [6, 8, 7]]
    eightPuzzle = EightPuzzle(state)
    self.assertEqual(eightPuzzle.find_blank(state), None)
```

**test_find_blank_5**: `unstated`
- reason: The docstring says the method returns the coordinates of the 0 element but never says what to return when the grid contains no 0, which is the case this test checks (it expects None).
- missing: The docstring should state what the method returns when no element equals 0 in the grid (for example, None), rather than only describing the case where a 0 exists.

```python
def test_find_blank_5(self):
    state = [[2, 3, 4], [5, 8, 1], [6, 8, 7]]
    eightPuzzle = EightPuzzle(state)
    self.assertEqual(eightPuzzle.find_blank(state), None)
```

## Method `move`

### Docstring

```python
def move(self, state, direction):
        """
        Find the blank block, then makes the board moves forward the given direction.
        :param state: a 3*3 size list of Integer, stores the state before moving.
        :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        >>> eightPuzzle.move([[2, 3, 4], [5, 8, 1], [6, 0, 7]], 'left')
        [[2, 3, 4], [5, 8, 1], [0, 6, 7]]
        """
```

### Reference code (`solution_code`)

```python
def move(self, state, direction):
        i, j = self.find_blank(state)
        new_state = [row[:] for row in state]

        if direction == 'up':
            new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
        elif direction == 'down':
            new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
        elif direction == 'left':
            new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
        elif direction == 'right':
            new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]

        return new_state
```

### Tests (`EightPuzzleTestMove`)

setUp (runs before each test):

```python
def setUp(self):
    self.initial_state = [[2, 3, 4], [5, 0, 1], [6, 8, 7]]
    self.eightPuzzle = EightPuzzle(self.initial_state)
```

**test_move_1**: `stated`
- reason: The docstring's example shows that 'left' moves the blank tile to the left, which matches the test's 'up' move putting the blank in the row above, so a programmer following it would pass.

```python
def test_move_1(self):
    result = self.eightPuzzle.move(self.initial_state, 'up')
    expected = [[2, 0, 4], [5, 3, 1], [6, 8, 7]]
    self.assertEqual(result, expected)
```

**test_move_2**: `stated`
- reason: The docstring's example shows that 'left' moves the blank tile left (swapping it with the tile to its left), so a programmer following that convention would produce the expected result for 'down' (blank swaps with the tile below it).

```python
def test_move_2(self):
    result = self.eightPuzzle.move(self.initial_state, 'down')
    expected = [[2, 3, 4], [5, 8, 1], [6, 0, 7]]
    self.assertEqual(result, expected)
```

**test_move_3**: `stated`
- reason: The docstring's example shows that 'left' moves the blank block one cell left, swapping it with the tile on its left, which is exactly what this test expects from a blank in the centre.

```python
def test_move_3(self):
    result = self.eightPuzzle.move(self.initial_state, 'left')
    expected = [[2, 3, 4], [0, 5, 1], [6, 8, 7]]
    self.assertEqual(result, expected)
```

**test_move_4**: `stated`
- reason: The docstring example shows that 'left' moves the blank block one cell left, so a programmer would also move the blank one cell right here, giving the expected [[2, 3, 4], [5, 1, 0], [6, 8, 7]].

```python
def test_move_4(self):
    result = self.eightPuzzle.move(self.initial_state, 'right')
    expected = [[2, 3, 4], [5, 1, 0], [6, 8, 7]]
    self.assertEqual(result, expected)
```

**test_move_5**: `unstated`
- reason: The docstring says direction only takes four values but does not say what happens for any other value, while the test passes '???' and expects the board returned unchanged, which a programmer could easily get wrong by raising an error.
- missing: The docstring should state what the method returns when the direction is not one of the allowed values, for example whether it returns an unchanged copy of the state or raises an error.

```python
def test_move_5(self):
    result = self.eightPuzzle.move(self.initial_state, '???')
    expected = [[2, 3, 4], [5, 0, 1], [6, 8, 7]]
    self.assertEqual(result, expected)
```

## Method `get_possible_moves`

### Docstring

```python
def get_possible_moves(self, state):
        """
        According the current state, find all the possible moving directions. Only has 4 direction 'up', 'down', 'left', 'right'.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return moves: a list of str, store all the possible moving directions according to the current state.
        >>> eightPuzzle.get_possible_moves([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        ['up', 'left', 'right']
        """
```

### Reference code (`solution_code`)

```python
def get_possible_moves(self, state):
        moves = []
        i, j = self.find_blank(state)

        if i > 0:
            moves.append('up')
        if i < 2:
            moves.append('down')
        if j > 0:
            moves.append('left')
        if j < 2:
            moves.append('right')

        return moves
```

### Tests (`EightPuzzleTestGetPossibleMoves`)

**test_get_possible_moves_1**: `stated`
- reason: The docstring says to return every direction the blank tile can move in a 3x3 grid, which covers the centre-blank case this test checks, so a programmer following it would return all four directions and pass.

```python
def test_get_possible_moves_1(self):
    eightPuzzle = EightPuzzle(None)
    state = [[2, 3, 4], [5, 0, 1], [6, 8, 7]]
    result = eightPuzzle.get_possible_moves(state)
    expected = ['up', 'down', 'left', 'right']
    for direction in result:
        self.assertIn(direction, expected)
```

**test_get_possible_moves_2**: `stated`
- reason: The docstring gives the blank-position rule for allowed directions and an example with the same state, so a programmer following it would return ['up', 'left', 'right'] and pass the test's subset check.

```python
def test_get_possible_moves_2(self):
    eightPuzzle = EightPuzzle(None)
    state = [[2, 3, 4], [5, 8, 1], [6, 0, 7]]
    result = eightPuzzle.get_possible_moves(state)
    expected = ['up', 'left', 'right']
    for direction in result:
        self.assertIn(direction, expected)
```

**test_get_possible_moves_3**: `stated`
- reason: The docstring asks for all possible moving directions from the current state, and its example (blank in the bottom row gives up/left/right) shows that moves off the board are excluded, so a programmer would produce ['down', 'left', 'right'] for a blank in the top-middle cell, matching the test.

```python
def test_get_possible_moves_3(self):
    eightPuzzle = EightPuzzle(None)
    state = [[2, 0, 4], [5, 3, 1], [6, 8, 7]]
    result = eightPuzzle.get_possible_moves(state)
    expected = ['down', 'left', 'right']
    for direction in result:
        self.assertIn(direction, expected)
```

**test_get_possible_moves_4**: `stated`
- reason: The docstring says moves are found from the current state and the example shows edge-dependent output (blank in the bottom middle yields up, left, right), so a programmer would produce up, down, left for a blank in the middle-right cell, which the test accepts.

```python
def test_get_possible_moves_4(self):
    eightPuzzle = EightPuzzle(None)
    state = [[2, 3, 4], [5, 1, 0], [6, 8, 7]]
    result = eightPuzzle.get_possible_moves(state)
    expected = ['up', 'down', 'left']
    for direction in result:
        self.assertIn(direction, expected)
```

**test_get_possible_moves_5**: `stated`
- reason: The docstring says to return all legal moving directions for the blank tile's position, and this test's blank at row 1, column 0 should yield up, down and right, which a programmer following the docstring would produce.

```python
def test_get_possible_moves_5(self):
    eightPuzzle = EightPuzzle(None)
    state = [[2, 3, 4], [0, 5, 1], [6, 8, 7]]
    result = eightPuzzle.get_possible_moves(state)
    expected = ['up', 'down', 'right']
    for direction in result:
        self.assertIn(direction, expected)
```

## Method `solve`

### Docstring

```python
def solve(self):
        """
        Use BFS algorithm to find the path solution which makes the initial state to the goal method.
        Maintain a list as a queue, named as open_list, append the initial state.
        Always visit and pop the 0 index element, invoke get_possible_moves method find all the possible directions.
        Traversal the possible_moves list and invoke move method to get several new states.Then append them.
        redo the above steps until the open_list is empty or the state has changed to the goal state.
        :return path: list of str, the solution to the goal state.
        >>> eightPuzzle = EightPuzzle([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
        >>> eightPuzzle.solve()
        ['right']
        """
```

### Reference code (`solution_code`)

```python
def solve(self):
        open_list = [(self.initial_state, [])]
        closed_list = []

        while open_list:
            current_state, path = open_list.pop(0)
            closed_list.append(current_state)

            if current_state == self.goal_state:
                return path

            for move in self.get_possible_moves(current_state):
                new_state = self.move(current_state, move)
                if new_state not in closed_list:
                    open_list.append((new_state, path + [move]))

        return None
```

### Tests (`EightPuzzleTestSolve`)

**test_solve_1**: `stated`
- reason: The docstring's own example runs solve() on the same initial board and gives ['right'], which is exactly the value this test asserts.

```python
def test_solve_1(self):
    eightPuzzle = EightPuzzle([[1, 2, 3], [4, 5, 6], [7, 0, 8]])
    result = eightPuzzle.solve()
    expected = ['right']
    self.assertEqual(result, expected)
```

**test_solve_2**: `stated`
- reason: The docstring says to use BFS from the initial state until the goal is reached, which yields the unique shortest two-move solution that this test expects, and the example shows the "blank moves in this direction" naming convention.

```python
def test_solve_2(self):
    eightPuzzle = EightPuzzle([[1, 2, 3], [4, 0, 6], [7, 5, 8]])
    result = eightPuzzle.solve()
    expected = ['down', 'right']
    self.assertEqual(result, expected)
```

**test_solve_3**: `unstated`
- reason: The docstring says to use BFS and return a path, but it does not say in what order candidate moves are tried, so a correct BFS could return a different equally short solution than the one the test expects.
- missing: The docstring should specify the order in which the possible moves from each state are generated and enqueued, since that order determines which of several equal-length shortest solutions is returned.

```python
def test_solve_3(self):
    eightPuzzle = EightPuzzle([[1, 2, 3], [0, 4, 5], [6, 7, 8]])
    result = eightPuzzle.solve()
    expected = ['right', 'right', 'down', 'left', 'left', 'up', 'right', 'down', 'right', 'up', 'left', 'left', 'down', 'right', 'right']
    self.assertEqual(result, expected)
```

**test_solve_4**: `unstated`
- reason: The docstring's loop, which checks for the goal only after moves are generated, does not say whether an already-solved initial state returns an empty path, so a correct implementation could instead expand moves and return a non-empty path.
- missing: The docstring should state what `solve` returns when the initial state already equals the goal state, such as an empty list of moves.

```python
def test_solve_4(self):
    eightPuzzle = EightPuzzle([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
    result = eightPuzzle.solve()
    expected = []
    self.assertEqual(result, expected)
```

**test_solve_5**: `stated`
- reason: The docstring describes a BFS that returns the path to the goal, and its example confirms that "right" means the blank tile moves right, so a BFS implementation would return the shortest path ['right', 'right'] that this test expects.

```python
def test_solve_5(self):
    eightPuzzle = EightPuzzle([[1, 2, 3], [4, 5, 6], [0, 7, 8]])
    result = eightPuzzle.solve()
    expected = ['right', 'right']
    self.assertEqual(result, expected)
```

**test_solve_6**: `unstated`
- reason: The docstring says the method returns a list of str moves but never says what to return when no path to the goal exists, which is the case this test checks (an all-zero board expecting None).
- missing: The docstring should state the return value when the search exhausts all reachable states without reaching the goal, for example that it returns None when no solution exists.

```python
def test_solve_6(self):
    eightPuzzle = EightPuzzle([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    result = eightPuzzle.solve()
    expected = None
    self.assertEqual(result, expected)
```
