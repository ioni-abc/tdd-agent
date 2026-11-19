import unittest


import unittest

class AgentTest_create_board(unittest.TestCase):

    def test_create_board_1(self):
        # Spec example: 4x4 board with icons ['a', 'b', 'c'] produces the documented layout.
        mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        expected = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        self.assertEqual(mc.create_board(), expected)

    def test_create_board_2(self):
        # The returned board has BOARD_SIZE[0] rows, each with BOARD_SIZE[1] columns (non-square).
        mc = MahjongConnect([3, 5], ['x', 'y'])
        board = mc.create_board()
        self.assertIsInstance(board, list)
        self.assertEqual(len(board), 3)
        for row in board:
            self.assertIsInstance(row, list)
            self.assertEqual(len(row), 5)

    def test_create_board_3(self):
        # Every cell of the board contains one of the given icons.
        icons = ['p', 'q', 'r', 's']
        mc = MahjongConnect([4, 6], icons)
        board = mc.create_board()
        for row in board:
            for cell in row:
                self.assertIn(cell, icons)

    def test_create_board_4(self):
        # With a single icon, every cell of the board must be that icon.
        mc = MahjongConnect([3, 2], ['z'])
        board = mc.create_board()
        self.assertEqual(board, [['z', 'z'],
                                 ['z', 'z'],
                                 ['z', 'z']])

    def test_create_board_5(self):
        # Rows are lists of the icons (not empty placeholders), and the board
        # is returned by create_board for a 2x3 board with two icons.
        mc = MahjongConnect([2, 3], ['m', 'n'])
        board = mc.create_board()
        self.assertEqual(len(board), 2)
        for row in board:
            self.assertEqual(len(row), 3)
            for cell in row:
                self.assertIsInstance(cell, str)
                self.assertIn(cell, ['m', 'n'])

import unittest

class AgentTest_has_path(unittest.TestCase):

    def test_has_path_1(self):
        # Spec example: the two icons at (0, 0) and (1, 0) in the documented
        # 4x4 board are vertically adjacent, so a path exists between them.
        mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        self.assertTrue(mc.has_path((0, 0), (1, 0)))

    def test_has_path_2(self):
        # Two icons on the same row, separated only by empty cells (' '),
        # are connected by a straight path through those empty cells.
        mc = MahjongConnect([1, 4], ['a'])
        mc.board = [['a', ' ', ' ', 'a']]
        self.assertTrue(mc.has_path((0, 0), (0, 3)))

    def test_has_path_3(self):
        # Two icons in the same column, separated only by empty cells,
        # are connected by a vertical path.
        mc = MahjongConnect([4, 1], ['a'])
        mc.board = [['a'],
                    [' '],
                    [' '],
                    ['a']]
        self.assertTrue(mc.has_path((0, 0), (3, 0)))

    def test_has_path_4(self):
        # The corner icons at (0, 0) and (0, 2) are fully enclosed by other
        # icons, so no path exists between them.
        mc = MahjongConnect([3, 3], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'a'],
                    ['b', 'c', 'b'],
                    ['c', 'b', 'c']]
        self.assertFalse(mc.has_path((0, 0), (0, 2)))

    def test_has_path_5(self):
        # A path between two icons is independent of the order of the
        # positions: has_path(pos1, pos2) matches has_path(pos2, pos1).
        mc = MahjongConnect([1, 4], ['a'])
        mc.board = [['a', ' ', ' ', 'a']]
        self.assertEqual(mc.has_path((0, 0), (0, 3)),
                         mc.has_path((0, 3), (0, 0)))
        self.assertTrue(mc.has_path((0, 3), (0, 0)))

import unittest

class AgentTest_is_valid_move(unittest.TestCase):

    def test_is_valid_move_1(self):
        # Spec example: (0, 0) and (1, 0) hold the same icon 'a' on the documented
        # 4x4 board and are vertically adjacent, so the move is valid.
        mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        self.assertTrue(mc.is_valid_move((0, 0), (1, 0)))

    def test_is_valid_move_2(self):
        # The two positions must not be the same, so selecting one icon twice is invalid.
        mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        self.assertFalse(mc.is_valid_move((0, 0), (0, 0)))

    def test_is_valid_move_3(self):
        # Positions must be within the game board range; (4, 0) lies outside a 4x4 board.
        mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        self.assertFalse(mc.is_valid_move((0, 0), (4, 0)))

    def test_is_valid_move_4(self):
        # The two positions must hold the same icon; 'a' and 'b' are adjacent
        # but different icons, so the move is invalid.
        mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        self.assertFalse(mc.is_valid_move((0, 0), (0, 1)))

    def test_is_valid_move_5(self):
        # Same icon at both positions, but the corners are fully enclosed by
        # other icons, so there is no valid path and the move is invalid.
        mc = MahjongConnect([3, 3], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'a'],
                    ['b', 'c', 'b'],
                    ['c', 'b', 'c']]
        self.assertFalse(mc.is_valid_move((0, 0), (0, 2)))

import unittest

class AgentTest_remove_icons(unittest.TestCase):

    def test_remove_icons_1(self):
        # Spec example: removing the vertically adjacent icons at (0, 0) and (1, 0)
        # from the documented 4x4 board blanks those two cells and leaves the rest unchanged.
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

    def test_remove_icons_2(self):
        # The method returns None according to its specification.
        mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        self.assertIsNone(mc.remove_icons((0, 0), (1, 0)))

    def test_remove_icons_3(self):
        # Two icons on the same row connected through empty cells are both removed,
        # leaving the whole row blank.
        mc = MahjongConnect([1, 4], ['a'])
        mc.board = [['a', ' ', ' ', 'a']]
        mc.remove_icons((0, 0), (0, 3))
        self.assertEqual(mc.board, [[' ', ' ', ' ', ' ']])

    def test_remove_icons_4(self):
        # Two icons in the same column connected through empty cells are both removed,
        # leaving the whole column blank.
        mc = MahjongConnect([4, 1], ['a'])
        mc.board = [['a'],
                    [' '],
                    [' '],
                    ['a']]
        mc.remove_icons((0, 0), (3, 0))
        self.assertEqual(mc.board, [[' '],
                                    [' '],
                                    [' '],
                                    [' ']])

    def test_remove_icons_5(self):
        # Removing a horizontally adjacent pair of matching icons blanks exactly those
        # two cells; the other icons on the board stay in place.
        mc = MahjongConnect([2, 2], ['a', 'b'])
        mc.board = [['a', 'a'],
                    ['b', 'b']]
        mc.remove_icons((0, 0), (0, 1))
        self.assertEqual(mc.board, [[' ', ' '],
                                    ['b', 'b']])
        remaining = sum(1 for row in mc.board for cell in row if cell != ' ')
        self.assertEqual(remaining, 2)

import unittest

class AgentTest_is_game_over(unittest.TestCase):

    def test_is_game_over_1(self):
        # Spec example: a 4x4 board where every cell is blank (' ') has no icons left,
        # so the game is over.
        mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [[' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' ']]
        self.assertTrue(mc.is_game_over())

    def test_is_game_over_2(self):
        # A full board of icons (the documented starting layout) still has icons on it,
        # so the game is not over.
        mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a'],
                    ['a', 'b', 'c', 'a']]
        self.assertFalse(mc.is_game_over())

    def test_is_game_over_3(self):
        # Even a single remaining icon means there are still icons on the board,
        # so the game is not over.
        mc = MahjongConnect([4, 4], ['a', 'b', 'c'])
        mc.board = [[' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', ' '],
                    [' ', ' ', ' ', 'c']]
        self.assertFalse(mc.is_game_over())

    def test_is_game_over_4(self):
        # After the only matching pair on the board is removed with remove_icons,
        # no icons remain, so the game is over.
        mc = MahjongConnect([1, 2], ['a'])
        mc.board = [['a', 'a']]
        mc.remove_icons((0, 0), (0, 1))
        self.assertTrue(mc.is_game_over())

    def test_is_game_over_5(self):
        # On a non-square board, an icon left in the last cell (bottom-right)
        # means the game is not over, even though every other cell is blank.
        mc = MahjongConnect([2, 3], ['m', 'n'])
        mc.board = [[' ', ' ', ' '],
                    [' ', ' ', 'n']]
        self.assertFalse(mc.is_game_over())