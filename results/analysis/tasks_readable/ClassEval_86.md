# ClassEval_86

## Skeleton (what the agent sees)

```python
class TicTacToe:
    """
    The class represents a game of Tic-Tac-Toe and its functions include making a move on the board, checking for a winner, and determining if the board is full.
    """

    def __init__(self, N=3):
        """
        Initialize a 3x3 game board with all empty spaces and current symble player, default is 'X'.
        """
        self.board = [[' ' for _ in range(N)] for _ in range(3)]
        self.current_player = 'X'

    def make_move(self, row, col):
        """
        Place the current player's mark at the specified position on the board and switch the mark.
        :param row: int, the row index of the position
        :param col: int, the column index of the position
        :return: bool, indicating whether the move was successful or not
        >>> ttt.current_player
        'X'
        >>> ttt.make_move(1, 1)
        >>> ttt.current_player
        'O'
        """

    def check_winner(self):
        """
        Check if there is a winner on the board in rows, columns and diagonals three directions
        :return: str or None, the mark of the winner ('X' or 'O'), or None if there is no winner yet
        >>> moves = [(1, 0), (2, 0), (1, 1), (2, 1), (1, 2)]
        >>> for move in moves:
        ...     ttt.make_move(move[0], move[1])
        >>> ttt.check_winner()
        'X'
        """

    def is_board_full(self):
        """
        Check if the game board is completely filled.
        :return: bool, indicating whether the game board is full or not
        >>> ttt.is_board_full()
        False
        """
```

## Method `make_move`

### Docstring

```python
def make_move(self, row, col):
        """
        Place the current player's mark at the specified position on the board and switch the mark.
        :param row: int, the row index of the position
        :param col: int, the column index of the position
        :return: bool, indicating whether the move was successful or not
        >>> ttt.current_player
        'X'
        >>> ttt.make_move(1, 1)
        >>> ttt.current_player
        'O'
        """
```

### Reference code (`solution_code`)

```python
def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        else:
            return False
```

### Tests (`TicTacToeTestMakeMove`)

**test_make_move_1**: `stated`
- reason: The docstring says the method places the current mark, switches players, and returns a success bool, so a programmer following it would return True and switch from X to O on an empty cell, which is what the test checks.

```python
def test_make_move_1(self):
    ttt = TicTacToe()
    self.assertEqual(ttt.current_player, 'X')
    self.assertTrue(ttt.make_move(0, 0))
    self.assertEqual(ttt.current_player, 'O')
```

**test_make_move_2**: `unstated`
- reason: The docstring says the method returns whether the move succeeded but never says that a move onto an occupied cell fails, or that a failed move leaves the current player unchanged, which is what the test checks.
- missing: The docstring should say that a move to a cell that is already occupied returns False, leaves the board unchanged, and does not switch the current player, while a move to an empty cell returns True and switches the player.

```python
def test_make_move_2(self):
    ttt = TicTacToe()
    self.assertEqual(ttt.current_player, 'X')
    self.assertTrue(ttt.make_move(0, 0))
    self.assertTrue(ttt.make_move(0, 1))
    self.assertFalse(ttt.make_move(0, 0))
    self.assertEqual(ttt.current_player, 'X')
```

**test_make_move_3**: `stated`
- reason: The docstring says the method places the current player's mark, switches players, and returns whether the move succeeded, so a programmer following it would return True for each move on an empty cell and end with the other player as current.

```python
def test_make_move_3(self):
    ttt = TicTacToe()
    self.assertEqual(ttt.current_player, 'X')
    self.assertTrue(ttt.make_move(0, 0))
    self.assertTrue(ttt.make_move(0, 1))
    self.assertTrue(ttt.make_move(1, 1))
    self.assertEqual(ttt.current_player, 'O')
```

**test_make_move_4**: `stated`
- reason: The docstring says each move places the current mark, switches the mark, and returns True on success, so a programmer would make four successful moves on empty cells and end with 'X' as the current player, which is what the test checks.

```python
def test_make_move_4(self):
    ttt = TicTacToe()
    self.assertEqual(ttt.current_player, 'X')
    self.assertTrue(ttt.make_move(0, 0))
    self.assertTrue(ttt.make_move(0, 1))
    self.assertTrue(ttt.make_move(1, 1))
    self.assertTrue(ttt.make_move(1, 2))
    self.assertEqual(ttt.current_player, 'X')
```

**test_make_move_5**: `stated`
- reason: The docstring says the method places the current player's mark, switches players, and returns whether the move succeeded, so a programmer following it would return True and alternate players for five moves on empty cells, which is what the test checks.

```python
def test_make_move_5(self):
    ttt = TicTacToe()
    self.assertEqual(ttt.current_player, 'X')
    self.assertTrue(ttt.make_move(0, 0))
    self.assertTrue(ttt.make_move(0, 1))
    self.assertTrue(ttt.make_move(1, 1))
    self.assertTrue(ttt.make_move(1, 2))
    self.assertTrue(ttt.make_move(2, 2))
    self.assertEqual(ttt.current_player, 'O')
```

## Method `check_winner`

### Docstring

```python
def check_winner(self):
        """
        Check if there is a winner on the board in rows, columns and diagonals three directions
        :return: str or None, the mark of the winner ('X' or 'O'), or None if there is no winner yet
        >>> moves = [(1, 0), (2, 0), (1, 1), (2, 1), (1, 2)]
        >>> for move in moves:
        ...     ttt.make_move(move[0], move[1])
        >>> ttt.check_winner()
        'X'
        """
```

### Reference code (`solution_code`)

```python
def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        return None
```

### Tests (`TicTacToeTestCheckWinner`)

**test_check_winner_1**: `stated`
- reason: The docstring's own example uses the same five moves and shows `check_winner()` returning `'X'`, so a programmer following it would get the expected result.

```python
def test_check_winner_1(self):
    ttt = TicTacToe()
    moves = [(1, 0), (2, 0), (1, 1), (2, 1), (1, 2)]
    for move in moves:
        ttt.make_move(move[0], move[1])
    self.assertEqual(ttt.check_winner(), 'X')
```

**test_check_winner_2**: `stated`
- reason: The docstring says the method checks rows, columns and diagonals and returns the winner's mark, so a programmer would return 'X' for three X's down column 0 as this test expects.

```python
def test_check_winner_2(self):
    ttt = TicTacToe()
    moves = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)]
    for move in moves:
        ttt.make_move(move[0], move[1])
    self.assertEqual(ttt.check_winner(), 'X')
```

**test_check_winner_3**: `stated`
- reason: The docstring says the method checks rows, columns and diagonals for a winning mark, and this test expects 'X' from a win along the main diagonal, which a programmer would detect.

```python
def test_check_winner_3(self):
    ttt = TicTacToe()
    moves = [(0, 0), (0, 1), (1, 1), (0, 2), (2, 2)]
    for move in moves:
        ttt.make_move(move[0], move[1])
    self.assertEqual(ttt.check_winner(), 'X')
```

**test_check_winner_4**: `stated`
- reason: The docstring says a winner is found in rows, columns and diagonals and that the mark ('X' or 'O') is returned, so a programmer would detect X's anti-diagonal (0,2),(1,1),(2,0) and return 'X', which is what the test expects.

```python
def test_check_winner_4(self):
    ttt = TicTacToe()
    moves = [(0, 2), (0, 1), (1, 1), (1, 0), (2, 0)]
    for move in moves:
        ttt.make_move(move[0], move[1])
    self.assertEqual(ttt.check_winner(), 'X')
```

**test_check_winner_5**: `stated`
- reason: The docstring says the method returns None when there is no winner yet, and this test's board has no completed row, column, or diagonal, so a programmer following the docstring would return None and pass.

```python
def test_check_winner_5(self):
    ttt = TicTacToe()
    moves = [(0, 0), (0, 1), (1, 1), (1, 0), (2, 0)]
    for move in moves:
        ttt.make_move(move[0], move[1])
    self.assertEqual(ttt.check_winner(), None)
```

## Method `is_board_full`

### Docstring

```python
def is_board_full(self):
        """
        Check if the game board is completely filled.
        :return: bool, indicating whether the game board is full or not
        >>> ttt.is_board_full()
        False
        """
```

### Reference code (`solution_code`)

```python
def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True
```

### Tests (`TicTacToeTestIsBoardFull`)

**test_is_board_full_1**: `stated`
- reason: A programmer reading "check if the game board is completely filled" and the example `ttt.is_board_full()` returning `False` would naturally return False for a freshly created, empty board, which is what the test checks.

```python
def test_is_board_full_1(self):
    ttt = TicTacToe()
    self.assertFalse(ttt.is_board_full())
```

**test_is_board_full_2**: `stated`
- reason: The docstring says the method checks whether the board is completely filled and returns a bool, so a programmer would return True once every cell is occupied, which is what this test expects after nine moves.

```python
def test_is_board_full_2(self):
    ttt = TicTacToe()
    moves = [(1, 1), (0, 2), (2, 2), (0, 0), (0, 1), (2, 1), (1, 0), (1, 2), (2, 0)]
    for move in moves:
        ttt.make_move(move[0], move[1])
    self.assertTrue(ttt.is_board_full())
```

**test_is_board_full_3**: `stated`
- reason: The docstring says the method returns whether the board is completely filled, so a programmer would return False when empty cells remain, which is what this test checks (5 of 9 cells filled, expects False).

```python
def test_is_board_full_3(self):
    ttt = TicTacToe()
    moves = [(0, 0), (0, 1), (1, 1), (1, 0), (2, 0)]
    for move in moves:
        ttt.make_move(move[0], move[1])
    self.assertFalse(ttt.is_board_full())
```

**test_is_board_full_4**: `stated`
- reason: The docstring says the method checks whether the board is completely filled and returns a bool, so a programmer would return True when all nine cells are occupied, which is what this test expects.

```python
def test_is_board_full_4(self):
    ttt = TicTacToe()
    moves = [(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (0, 2), (1, 2), (2, 1), (2, 2)]
    for move in moves:
        ttt.make_move(move[0], move[1])
    self.assertTrue(ttt.is_board_full())
```

**test_is_board_full_5**: `stated`
- reason: The docstring says the method checks whether the board is completely filled, so a programmer would return False when any cell is still empty, which matches the test's expected False with one cell left open.

```python
def test_is_board_full_5(self):
    ttt = TicTacToe()
    moves = [(0, 0), (0, 1), (1, 1), (1, 0), (2, 0), (0, 2), (1, 2), (2, 1)]
    for move in moves:
        ttt.make_move(move[0], move[1])
    self.assertFalse(ttt.is_board_full())
```

## Tests in no method's test class

### `TicTacToeTestMain`

**test_main**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_main(self):
    # A draw down way
    ttt = TicTacToe()
    moves = [(1, 1), (0, 2), (2, 2), (0, 0), (0, 1), (2, 1), (1, 0), (1, 2), (2, 0)]
    for move in moves:
        self.assertTrue(ttt.make_move(move[0], move[1]))
        # no winner in this case
        self.assertFalse(ttt.check_winner())
        if move != (2, 0):
            self.assertFalse(ttt.is_board_full())
    self.assertTrue(ttt.is_board_full())
```
