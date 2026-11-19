import unittest


import unittest

import itertools

class AgentTest_generate_mine_sweeper_map(unittest.TestCase):

    @staticmethod
    def _neighbours(n, r, c):
        for dr, dc in itertools.product((-1, 0, 1), repeat=2):
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                yield nr, nc

    @staticmethod
    def _expected_board(n, mines):
        board = []
        for r in range(n):
            row = []
            for c in range(n):
                if (r, c) in mines:
                    row.append('X')
                else:
                    count = sum(
                        1 for nr, nc in AgentTest_generate_mine_sweeper_map._neighbours(n, r, c)
                        if (nr, nc) in mines
                    )
                    row.append(count)
            board.append(row)
        return board

    def test_generate_mine_sweeper_map_1(self):
        # The map is an n*n board: n rows, each with n entries.
        game = MinesweeperGame(3, 1)
        board = game.generate_mine_sweeper_map()
        self.assertIsInstance(board, list)
        self.assertEqual(len(board), 3)
        for row in board:
            self.assertIsInstance(row, list)
            self.assertEqual(len(row), 3)

    def test_generate_mine_sweeper_map_2(self):
        # Exactly k cells are mines, marked with 'X'.
        n, k = 5, 7
        game = MinesweeperGame(n, k)
        board = game.generate_mine_sweeper_map()
        mine_count = sum(1 for row in board for cell in row if cell == 'X')
        self.assertEqual(mine_count, k)

    def test_generate_mine_sweeper_map_3(self):
        # Every non-mine cell holds the number of mines among its surrounding cells,
        # and mine cells remain 'X'.
        n, k = 6, 10
        game = MinesweeperGame(n, k)
        board = game.generate_mine_sweeper_map()
        for r in range(n):
            for c in range(n):
                if board[r][c] == 'X':
                    continue
                expected = sum(
                    1 for nr, nc in self._neighbours(n, r, c) if board[nr][nc] == 'X'
                )
                self.assertEqual(board[r][c], expected,
                                 msg=f"Wrong count at ({r}, {c})")

    def test_generate_mine_sweeper_map_4(self):
        # With no mines, every cell is 0.
        n = 4
        game = MinesweeperGame(n, 0)
        board = game.generate_mine_sweeper_map()
        self.assertEqual(board, [[0] * n for _ in range(n)])

    def test_generate_mine_sweeper_map_5(self):
        # For the 3x3 board with one mine, the result is a valid board for a single
        # mine placed at some cell, as in the docstring example [['X', 1, 0], [1, 1, 0], [0, 0, 0]].
        game = MinesweeperGame(3, 1)
        board = game.generate_mine_sweeper_map()
        valid_boards = [
            self._expected_board(3, {(r, c)})
            for r in range(3) for c in range(3)
        ]
        self.assertIn(board, valid_boards)

class AgentTest_generate_playerMap(unittest.TestCase):

    def test_generate_playerMap_1(self):
        # The player map is an n*n board: n rows, each with n entries.
        n = 4
        game = MinesweeperGame(n, 3)
        player_map = game.generate_playerMap()
        self.assertIsInstance(player_map, list)
        self.assertEqual(len(player_map), n)
        for row in player_map:
            self.assertIsInstance(row, list)
            self.assertEqual(len(row), n)

    def test_generate_playerMap_2(self):
        # Matches the docstring example: MinesweeperGame(3, 1) gives an all-'-' 3x3 board.
        game = MinesweeperGame(3, 1)
        self.assertEqual(
            game.generate_playerMap(),
            [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        )

    def test_generate_playerMap_3(self):
        # Every position is unknown, so every cell is the string '-'.
        n, k = 5, 7
        game = MinesweeperGame(n, k)
        player_map = game.generate_playerMap()
        for r in range(n):
            for c in range(n):
                self.assertIsInstance(player_map[r][c], str)
                self.assertEqual(player_map[r][c], '-',
                                 msg=f"Cell ({r}, {c}) should be unknown '-'")

    def test_generate_playerMap_4(self):
        # Edge case: a 1x1 board is a single unknown cell.
        game = MinesweeperGame(1, 0)
        self.assertEqual(game.generate_playerMap(), [['-']])

    def test_generate_playerMap_5(self):
        # The player map stored on the game at construction is the one produced
        # by generate_playerMap, and it contains no revealed numbers or mines.
        n, k = 6, 10
        game = MinesweeperGame(n, k)
        self.assertEqual(game.player_map, game.generate_playerMap())
        for row in game.player_map:
            for cell in row:
                self.assertNotIn(cell, (0, 1, 2, 3, 4, 5, 6, 7, 8, 'X'))
                self.assertEqual(cell, '-')

import unittest

class AgentTest_check_won(unittest.TestCase):

    def test_check_won_1(self):
        # Docstring example: nothing has been swept yet, so the game is not won.
        game = MinesweeperGame(3, 1)
        game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.assertIs(game.check_won(game.player_map), False)

    def test_check_won_2(self):
        # Every safe cell is revealed and only the mine position remains unknown: won.
        game = MinesweeperGame(3, 1)
        game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        player_map = [['-', 1, 0], [1, 1, 0], [0, 0, 0]]
        self.assertIs(game.check_won(player_map), True)

    def test_check_won_3(self):
        # A safe cell is still unknown alongside the mine, so the game is not won.
        game = MinesweeperGame(3, 1)
        game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        player_map = [['-', 1, 0], [1, 1, 0], [0, 0, '-']]
        self.assertIs(game.check_won(player_map), False)

    def test_check_won_4(self):
        # Two mines on a 2x2 board: revealing both safe cells and leaving only
        # the mine positions unknown means the game is won.
        game = MinesweeperGame(2, 2)
        game.minesweeper_map = [['X', 2], [2, 'X']]
        player_map = [['-', 2], [2, '-']]
        self.assertIs(game.check_won(player_map), True)

    def test_check_won_5(self):
        # check_won judges the map it is given, not the game's stored player_map.
        game = MinesweeperGame(3, 1)
        game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        winning_map = [['-', 1, 0], [1, 1, 0], [0, 0, 0]]
        self.assertIs(game.check_won(winning_map), True)

class AgentTest_sweep(unittest.TestCase):

    def test_sweep_1(self):
        # Docstring example: sweeping (1, 1) reveals the value 1 at that position only.
        game = MinesweeperGame(3, 1)
        game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.assertEqual(
            game.sweep(1, 1),
            [['-', '-', '-'], ['-', 1, '-'], ['-', '-', '-']]
        )

    def test_sweep_2(self):
        # Sweeping a numbered cell in the top row reveals only that cell's value.
        game = MinesweeperGame(3, 1)
        game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.assertEqual(
            game.sweep(0, 1),
            [['-', 1, '-'], ['-', '-', '-'], ['-', '-', '-']]
        )

    def test_sweep_3(self):
        # Sweeping the last safe cell leaves only the mine unknown, so the game is won.
        game = MinesweeperGame(3, 1)
        game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        game.player_map = [['-', 1, 0], [1, '-', 0], [0, 0, 0]]
        self.assertIs(game.sweep(1, 1), True)

    def test_sweep_4(self):
        # On a 2x2 board with two mines, sweeping one safe cell leaves the other
        # safe cell unknown, so the result is the updated player map, not a win.
        game = MinesweeperGame(2, 2)
        game.minesweeper_map = [['X', 2], [2, 'X']]
        game.player_map = [['-', '-'], ['-', '-']]
        self.assertEqual(game.sweep(0, 1), [['-', 2], ['-', '-']])

    def test_sweep_5(self):
        # The returned map keeps the same n*n shape and previously revealed cells.
        game = MinesweeperGame(3, 1)
        game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        game.player_map = [['-', 1, '-'], ['-', '-', '-'], ['-', '-', '-']]
        result = game.sweep(1, 1)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)
        for row in result:
            self.assertIsInstance(row, list)
            self.assertEqual(len(row), 3)
        self.assertEqual(result[0][1], 1)
        self.assertEqual(result[1][1], 1)