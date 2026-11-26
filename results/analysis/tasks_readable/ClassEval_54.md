# ClassEval_54

## Skeleton (what the agent sees)

```python
import random

class MahjongConnect:
    """
    MahjongConnect is a class representing a game board for Mahjong Connect with features like creating the board, checking valid moves, finding paths, removing icons, and checking if the game is over.
    """

    def __init__(self, BOARD_SIZE, ICONS):
        """
        initialize the board size and the icon list, create the game board
        :param BOARD_SIZE: list of two integer numbers, representing the number of rows and columns of the game board
        :param ICONS: list of string, representing the icons
        >>>mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.BOARD_SIZE = [4, 4]
        mc.ICONS = ['a', 'b', 'c']
        mc.board = mc.create_board()
        """
        self.BOARD_SIZE = BOARD_SIZE
        self.ICONS = ICONS
        self.board = self.create_board()

    def create_board(self):
        """
        create the game board with the given board size and icons
        :return: 2-dimensional list, the game board
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        >>> mc.create_board()
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        """

    def is_valid_move(self, pos1, pos2):
        """
        check if the move of two icons is valid (i.e. positions are within the game board range, the two positions are not the same, the two positions have the same icon, and there is a valid path between the two positions)
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return:True or False ,representing whether the move of two icons is valid
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        >>> mc.is_valid_move((0, 0), (1, 0))
        True
        """


    def has_path(self, pos1, pos2):
        """
        check if there is a path between two icons
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return: True or False ,representing whether there is a path between two icons
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        >>> mc.is_valid_move((0, 0), (1, 0))
        True
        """


    def remove_icons(self, pos1, pos2):
        """
        remove the connected icons on the game board
        :param pos1: position tuple(x, y) of the first icon to be removed
        :param pos2: position tuple(x, y) of the second icon to be removed
        :return: None
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        >>> mc.remove_icons((0, 0), (1, 0))
        mc.board = [[' ', 'b', 'c', 'a'],
                    [' ', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        """


    def is_game_over(self):
        """
        Check if the game is over (i.e., if there are no more icons on the game board)
        :return: True or False ,representing whether the game is over
        >>> mc = MahjongConnect([4, 4] ['a', 'b', 'c'])
        >>> mc.board = [[' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' ']]
        >>> mc.is_game_over()
        True
        """
```

## Method `create_board`

### Docstring

```python
def create_board(self):
        """
        create the game board with the given board size and icons
        :return: 2-dimensional list, the game board
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        >>> mc.create_board()
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        """
```

### Reference code (`solution_code`)

```python
def create_board(self):
        board = [[random.choice(self.ICONS) for _ in range(self.BOARD_SIZE[1])] for _ in range(self.BOARD_SIZE[0])]
        return board
```

### Tests (`MahjongConnectTestCreateBoard`)

**test_create_board_1**: `unstated`
- reason: The test requires the instance attributes `BOARD_SIZE` and `ICONS` to hold the constructor arguments under those exact names, which the docstring never mentions, so a correct implementation using other names would fail.
- missing: The docstring should name the attributes that store the board size and icon list (e.g. `self.BOARD_SIZE` and `self.ICONS`) and state that every cell is drawn from those icons.

```python
def test_create_board_1(self):
    mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    self.assertEqual(mc.BOARD_SIZE, [4, 4])
    self.assertEqual(mc.ICONS, ['a', 'b', 'c'])
    for row in mc.board:
        for icon in row:
            self.assertIn(icon, mc.ICONS)
```

**test_create_board_2**: `unstated`
- reason: The test checks that the constructor stores the board size and icons as attributes named `BOARD_SIZE` and `ICONS`, and the docstring never names these attributes, so a correct implementation using other names would fail.
- missing: The docstring should name the instance attributes that hold the board size and the icon list (and state that the board cells are drawn from those icons), so an implementation knows which attribute names to store.

```python
def test_create_board_2(self):
    mc = MahjongConnect([2, 2], ['a', 'b', 'c'])
    self.assertEqual(mc.BOARD_SIZE, [2, 2])
    self.assertEqual(mc.ICONS, ['a', 'b', 'c'])
    for row in mc.board:
        for icon in row:
            self.assertIn(icon, mc.ICONS)
```

**test_create_board_3**: `unstated`
- reason: The test checks that the instance keeps its size and icon attributes and stores the generated board on the instance, but the docstring only says the method returns a 2D list and never mentions storing state.
- missing: The docstring should state that the constructor's size and icon inputs are saved as instance attributes, and that the generated board is also saved on the instance, with every cell chosen from the given icons.

```python
def test_create_board_3(self):
    mc = MahjongConnect([3, 3], ['a', 'b', 'c'])
    self.assertEqual(mc.BOARD_SIZE, [3, 3])
    self.assertEqual(mc.ICONS, ['a', 'b', 'c'])
    for row in mc.board:
        for icon in row:
            self.assertIn(icon, mc.ICONS)
```

**test_create_board_4**: `unstated`
- reason: The test checks that the constructor stores the size and icons as `BOARD_SIZE` and `ICONS`, and the docstring never names those attributes, so a correct implementation using other names would fail.
- missing: The docstring should state that the constructor must store the board size and the icon list in attributes named `BOARD_SIZE` and `ICONS`, and that each cell is chosen at random from those icons.

```python
def test_create_board_4(self):
    mc = MahjongConnect([1, 1], ['a', 'b', 'c'])
    self.assertEqual(mc.BOARD_SIZE, [1, 1])
    self.assertEqual(mc.ICONS, ['a', 'b', 'c'])
    for row in mc.board:
        for icon in row:
            self.assertIn(icon, mc.ICONS)
```

**test_create_board_5**: `unstated`
- reason: The test checks that the constructor stores `BOARD_SIZE` and `ICONS` as attributes and that every cell is drawn from `ICONS`, but the docstring never mentions those attribute names or that cells are randomly chosen from the icons, and its example shows a fixed pattern a random board would not produce.
- missing: The docstring should state that the constructor stores the board size and icon list in attributes with the names the tests read, and that each cell of the returned board is a randomly chosen icon from that icon list, so the example output is only illustrative.

```python
def test_create_board_5(self):
    mc = MahjongConnect([5, 5], ['a', 'b', 'c'])
    self.assertEqual(mc.BOARD_SIZE, [5, 5])
    self.assertEqual(mc.ICONS, ['a', 'b', 'c'])
    for row in mc.board:
        for icon in row:
            self.assertIn(icon, mc.ICONS)
```

## Method `is_valid_move`

### Docstring

```python
def is_valid_move(self, pos1, pos2):
        """
        check if the move of two icons is valid (i.e. positions are within the game board range, the two positions are not the same, the two positions have the same icon, and there is a valid path between the two positions)
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return:True or False ,representing whether the move of two icons is valid
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        >>> mc.is_valid_move((0, 0), (1, 0))
        True
        """
```

### Reference code (`solution_code`)

```python
def is_valid_move(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2

        # Check if positions are within the game board range
        if not (0 <= x1 < self.BOARD_SIZE[0] and 0 <= y1 < self.BOARD_SIZE[1] and 0 <= x2 < self.BOARD_SIZE[
            0] and 0 <= y2 <
                self.BOARD_SIZE[1]):
            return False

        # Check if the two positions are the same
        if pos1 == pos2:
            return False

        # Check if the two positions have the same icon
        if self.board[x1][y1] != self.board[x2][y2]:
            return False

        # Check if there is a valid path between the two positions
        if not self.has_path(pos1, pos2):
            return False

        return True
```

### Tests (`MahjongConnectTestIsValidMove`)

**test_is_valid_move_1**: `stated`
- reason: The docstring says a move is valid when both positions are on the board, distinct, hold the same icon, and have a valid path, and the test's adjacent same-icon pair meets all of these and expects True.

```python
def test_is_valid_move_1(self):
    mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    res = mc.is_valid_move((0, 0), (1, 0))
    self.assertEqual(res, True)
```

**test_is_valid_move_2**: `stated`
- reason: The docstring requires that the two positions have the same icon, and the test's two positions hold different icons ('a' and 'b'), so a programmer following the docstring would return False as the test expects.

```python
def test_is_valid_move_2(self):
    mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    res = mc.is_valid_move((0, 0), (0, 1))
    self.assertEqual(res, False)
```

**test_is_valid_move_3**: `stated`
- reason: The docstring says a move is invalid when either position falls outside the game board range, so a programmer following it would return False for the out-of-range first position in this test.

```python
def test_is_valid_move_3(self):
    mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    res = mc.is_valid_move((-1, 0), (0, 1))
    self.assertEqual(res, False)
```

**test_is_valid_move_4**: `stated`
- reason: The docstring lists "the two positions are not the same" as a condition for a valid move, so a programmer would return False when both positions are identical, which is what the test checks.

```python
def test_is_valid_move_4(self):
    mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    res = mc.is_valid_move((0, 0), (0, 0))
    self.assertEqual(res, False)
```

**test_is_valid_move_5**: `stated`
- reason: The docstring says a valid move requires both positions to be within the game board range, so a programmer would return False for an out-of-range position, which is what the test expects.

```python
def test_is_valid_move_5(self):
    mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    res = mc.is_valid_move((300, 0), (0, 0))
    self.assertEqual(res, False)
```

**test_is_valid_move_6**: `stated`
- reason: The docstring requires a valid path between the two positions, and on this board the two 'a' cells sit in disconnected regions blocked by 'b' and 'c' icons, so a programmer checking for a path would correctly return False.

```python
def test_is_valid_move_6(self):
    mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [['a', 'b', 'a', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    res = mc.is_valid_move((0, 2), (0, 0))
    self.assertEqual(res, False)
```

## Method `has_path`

### Docstring

```python
def has_path(self, pos1, pos2):
        """
        check if there is a path between two icons
        :param pos1: position tuple(x, y) of the first icon
        :param pos2: position tuple(x, y) of the second icon
        :return: True or False ,representing whether there is a path between two icons
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        >>> mc.is_valid_move((0, 0), (1, 0))
        True
        """
```

### Reference code (`solution_code`)

```python
def has_path(self, pos1, pos2):
        visited = set()
        stack = [pos1]

        while stack:
            current_pos = stack.pop()
            if current_pos == pos2:
                return True

            if current_pos in visited:
                continue

            visited.add(current_pos)
            x, y = current_pos

            # Check adjacent positions (up, down, left, right)
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < self.BOARD_SIZE[0] and 0 <= new_y < self.BOARD_SIZE[1]:
                    if (new_x, new_y) not in visited and self.board[new_x][new_y] == self.board[x][y]:
                        stack.append((new_x, new_y))

        return False
```

### Tests (`MahjongConnectTestHasPath`)

**test_has_path_1**: `stated`
- reason: The docstring says has_path checks whether a path exists between two icons, and a programmer would naturally return True for two identical, orthogonally adjacent icons, which is exactly what this test checks.

```python
def test_has_path_1(self):
    mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    res = mc.has_path((0, 0), (1, 0))
    self.assertEqual(res, True)
```

**test_has_path_2**: `unstated`
- reason: The docstring defines a path only between two icons and never says whether a position counts as connected to itself, so a correct implementation that only searches outward from pos1 could return False where the test expects True.
- missing: The docstring should state whether two identical positions (pos1 equal to pos2) are considered connected, and what result to return in that case.

```python
def test_has_path_2(self):
    mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    res = mc.has_path((0, 0), (0, 0))
    self.assertEqual(res, True)
```

**test_has_path_3**: `stated`
- reason: The docstring says has_path returns True when there is a path between the two icons, and this test expects True for two matching icons joined by a straight run of same-icon cells, which a reasonable implementation of that description returns.

```python
def test_has_path_3(self):
    mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    res = mc.has_path((0, 0), (3, 0))
    self.assertEqual(res, True)
```

**test_has_path_4**: `unstated`
- reason: The docstring only says "check if there is a path between two icons" and never mentions that a path must run through cells holding the same icon, so a programmer could reasonably return True for connected cells of different icons, while the test expects False.
- missing: The docstring should state that a path exists only when every cell along it, including both endpoints, holds the same icon, and that paths move only to orthogonally adjacent cells of that same icon.

```python
def test_has_path_4(self):
    mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    res = mc.has_path((0, 0), (1, 1))
    self.assertEqual(res, False)
```

**test_has_path_5**: `unstated`
- reason: The test passes a position outside the board as the first icon and expects False, but the docstring says nothing about out-of-bounds positions, so a correct implementation could raise an IndexError instead.
- missing: The docstring should say what happens when either position lies outside the board (for example, that such a position has no path and the method returns False).

```python
def test_has_path_5(self):
    mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    res = mc.has_path((300, 0), (1, 1))
    self.assertEqual(res, False)
```

**test_has_path_6**: `stated`
- reason: The docstring asks whether a path exists between two icons, and on a board where every cell holds the same icon any reasonable connectivity rule (adjacent matching cells, or up to two turns) gives True for the corner-to-corner pair.

```python
def test_has_path_6(self):
    mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [['a', 'a', 'a', 'a'],
                ['a', 'a', 'a', 'a'],
                ['a', 'a', 'a', 'a'],
                ['a', 'a', 'a', 'a']]
    res = mc.has_path((0, 0), (3, 3))
    self.assertEqual(res, True)
```

## Method `remove_icons`

### Docstring

```python
def remove_icons(self, pos1, pos2):
        """
        remove the connected icons on the game board
        :param pos1: position tuple(x, y) of the first icon to be removed
        :param pos2: position tuple(x, y) of the second icon to be removed
        :return: None
        >>> mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        >>> mc.remove_icons((0, 0), (1, 0))
        mc.board = [[' ', 'b', 'c', 'a'],
                    [' ', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        """
```

### Reference code (`solution_code`)

```python
def remove_icons(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        self.board[x1][y1] = ' '
        self.board[x2][y2] = ' '
```

### Tests (`MahjongConnectTestRemoveIcons`)

**test_remove_icons_1**: `unstated`
- reason: The docstring says positions are (x, y) tuples but never says x is the row index, so a programmer using the usual Cartesian reading (x as column) would swap the cells and fail this test's expected board.
- missing: The docstring should state that each position is (row, column), i.e. the first element indexes the outer list of the board, and that a removed cell is set to a single space character ' '.

```python
def test_remove_icons_1(self):
    mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    mc.remove_icons((0, 0), (1, 0))
    self.assertEqual(mc.board, [[' ', 'b', 'c', 'a'],
                                [' ', 'b', 'c', 'a'],
                                ['a', 'b', 'c', 'a'],
                                ['a', 'b', 'c', 'a']])
```

**test_remove_icons_2**: `stated`
- reason: The docstring says each position is an (x, y) tuple of an icon to remove and that the method returns None, so a programmer would set board[x][y] to a blank for both positions, which is what this test checks.

```python
def test_remove_icons_2(self):
    mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    mc.remove_icons((2, 0), (1, 0))
    self.assertEqual(mc.board, [['a', 'b', 'c', 'a'],
                                [' ', 'b', 'c', 'a'],
                                [' ', 'b', 'c', 'a'],
                                ['a', 'b', 'c', 'a']])
```

**test_remove_icons_3**: `stated`
- reason: The docstring's example shows that removing the icons at the two given (x, y) positions replaces those cells with a blank, which is exactly what this test checks for a different pair of positions.

```python
def test_remove_icons_3(self):
    mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    mc.remove_icons((1, 1), (0, 1))
    self.assertEqual(mc.board, [['a', ' ', 'c', 'a'],
                                ['a', ' ', 'c', 'a'],
                                ['a', 'b', 'c', 'a'],
                                ['a', 'b', 'c', 'a']])
```

**test_remove_icons_4**: `stated`
- reason: The docstring says to remove the icons at the two given (x, y) positions, and its example shows that x indexes the row, so a programmer setting those two cells to blank would produce the test's expected board.

```python
def test_remove_icons_4(self):
    mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    mc.remove_icons((3, 0), (2, 0))
    self.assertEqual(mc.board, [['a', 'b', 'c', 'a'],
                                ['a', 'b', 'c', 'a'],
                                [' ', 'b', 'c', 'a'],
                                [' ', 'b', 'c', 'a']])
```

**test_remove_icons_5**: `stated`
- reason: The docstring says the method removes the icons at the two given (x, y) positions, and its example shows those cells becoming blank, so a programmer following it would set both positions to ' ' and pass this test.

```python
def test_remove_icons_5(self):
    mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    mc.remove_icons((3, 3), (2, 3))
    self.assertEqual(mc.board, [['a', 'b', 'c', 'a'],
                                ['a', 'b', 'c', 'a'],
                                ['a', 'b', 'c', ' '],
                                ['a', 'b', 'c', ' ']])
```

## Method `is_game_over`

### Docstring

```python
def is_game_over(self):
        """
        Check if the game is over (i.e., if there are no more icons on the game board)
        :return: True or False ,representing whether the game is over
        >>> mc = MahjongConnect([4, 4] ['a', 'b', 'c'])
        >>> mc.board = [[' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' '],
        >>>         [' ', ' ', ' ', ' ']]
        >>> mc.is_game_over()
        True
        """
```

### Reference code (`solution_code`)

```python
def is_game_over(self):
        for row in self.board:
            if any(icon != ' ' for icon in row):
                return False
        return True
```

### Tests (`MahjongConnectTestIsGameOver`)

**test_is_game_over_1**: `stated`
- reason: The docstring says the game is over when no icons remain on the board, and the test's all-blank board has no icons, so a correct implementation returns True.

```python
def test_is_game_over_1(self):
    mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [[' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ']]
    res = mc.is_game_over()
    self.assertEqual(res, True)
```

**test_is_game_over_2**: `stated`
- reason: The docstring says the game is over only when no icons remain on the board, so a programmer would return False when any non-blank icon is present, which is what this test checks.

```python
def test_is_game_over_2(self):
    mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [['a', ' ', ' ', ' '],
                ['a', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ']]
    res = mc.is_game_over()
    self.assertEqual(res, False)
```

**test_is_game_over_3**: `stated`
- reason: The docstring says the game is over only when there are no more icons on the board, so a board with one remaining icon should return False, which is what the test expects.

```python
def test_is_game_over_3(self):
    mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [[' ', ' ', ' ', ' '],
                ['a', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ']]
    res = mc.is_game_over()
    self.assertEqual(res, False)
```

**test_is_game_over_4**: `stated`
- reason: The docstring says the game is over only when there are no more icons on the board, so a board with a remaining icon should return False, which is what the test checks.

```python
def test_is_game_over_4(self):
    mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [['1', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ']]
    res = mc.is_game_over()
    self.assertEqual(res, False)
```

**test_is_game_over_5**: `stated`
- reason: The docstring says the game is over only when there are no more icons on the board, so a board with one remaining icon should return False, which is what the test expects.

```python
def test_is_game_over_5(self):
    mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    mc.board = [['a', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ']]
    res = mc.is_game_over()
    self.assertEqual(res, False)
```

## Tests in no method's test class

### `MahjongConnectTest`

**test_mahjongconnect**: `no_method_info`
- reason: its test class is in no methods_info[i]['test_class']

```python
def test_mahjongconnect(self):
    mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
    self.assertEqual(mc.BOARD_SIZE, [4, 4])
    self.assertEqual(mc.ICONS, ['a', 'b', 'c'])
    for row in mc.board:
        for icon in row:
            self.assertIn(icon, mc.ICONS)

    mc.board = [['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a'],
                ['a', 'b', 'c', 'a']]
    res = mc.is_valid_move((0, 0), (1, 0))
    self.assertEqual(res, True)

    res = mc.has_path((0, 0), (1, 0))
    self.assertEqual(res, True)

    mc.remove_icons((0, 0), (1, 0))
    self.assertEqual(mc.board, [[' ', 'b', 'c', 'a'],
                                [' ', 'b', 'c', 'a'],
                                ['a', 'b', 'c', 'a'],
                                ['a', 'b', 'c', 'a']])

    mc.board = [[' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ']]
    res = mc.is_game_over()
    self.assertEqual(res, True)
```
