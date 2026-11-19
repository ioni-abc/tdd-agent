import unittest



class MinesweeperGameTestGenerateMineSweeperMap(unittest.TestCase):
    def test_generate_mine_sweeper_map(self):
        minesweeper_game = MinesweeperGame(3, 2)
        length = len(minesweeper_game.minesweeper_map)
        mine_num = 0
        for row in minesweeper_game.minesweeper_map:
            for cell in row:
                if cell == 'X':
                    mine_num += 1
        self.assertEqual(3, length)
        self.assertEqual(2, mine_num)

    def test_generate_mine_sweeper_map_2(self):
        minesweeper_game = MinesweeperGame(3, 1)
        length = len(minesweeper_game.minesweeper_map)
        mine_num = 0
        for row in minesweeper_game.minesweeper_map:
            for cell in row:
                if cell == 'X':
                    mine_num += 1
        self.assertEqual(3, length)
        self.assertEqual(1, mine_num)

    def test_generate_mine_sweeper_map_3(self):
        minesweeper_game = MinesweeperGame(3, 0)
        length = len(minesweeper_game.minesweeper_map)
        mine_num = 0
        for row in minesweeper_game.minesweeper_map:
            for cell in row:
                if cell == 'X':
                    mine_num += 1
        self.assertEqual(3, length)
        self.assertEqual(0, mine_num)

import unittest

class AgentTest_generate_mine_sweeper_map(unittest.TestCase):
    def test_generate_mine_sweeper_map_1(self):
        minesweeper_game = MinesweeperGame(1, 1)
        self.assertEqual([['X']], minesweeper_game.minesweeper_map)

    def test_generate_mine_sweeper_map_2(self):
        n, k = 4, 5
        for _ in range(20):
            minesweeper_game = MinesweeperGame(n, k)
            board = minesweeper_game.minesweeper_map
            for r in range(n):
                for c in range(n):
                    cell = board[r][c]
                    if cell == 'X':
                        continue
                    neighbour_mines = 0
                    for dr in (-1, 0, 1):
                        for dc in (-1, 0, 1):
                            if dr == 0 and dc == 0:
                                continue
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 'X':
                                neighbour_mines += 1
                    self.assertEqual(neighbour_mines, cell)

class MinesweeperGameTestGeneratePlayerMap(unittest.TestCase):
    def test_generate_playerMap(self):
        minesweeper_game = MinesweeperGame(3, 2)
        self.assertEqual(minesweeper_game.generate_playerMap(), [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])

    def test_generate_playerMap_2(self):
        minesweeper_game = MinesweeperGame(3, 1)
        self.assertEqual(minesweeper_game.generate_playerMap(), [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])

    def test_generate_playerMap_3(self):
        minesweeper_game = MinesweeperGame(4, 2)
        self.assertEqual(minesweeper_game.generate_playerMap(),[['-', '-', '-', '-'],['-', '-', '-', '-'],['-', '-', '-', '-'],['-', '-', '-', '-']])

import unittest

class AgentTest_generate_playerMap(unittest.TestCase):
    def test_generate_playerMap_1(self):
        minesweeper_game = MinesweeperGame(1, 1)
        self.assertEqual([['-']], minesweeper_game.generate_playerMap())

    def test_generate_playerMap_2(self):
        minesweeper_game = MinesweeperGame(5, 0)
        self.assertEqual(
            [['-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-'],
             ['-', '-', '-', '-', '-']],
            minesweeper_game.generate_playerMap()
        )

class MinesweeperGameTestCheckWon(unittest.TestCase):
    def test_check_won(self):
        minesweeper_game = MinesweeperGame(3, 1)
        minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        minesweeper_game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.assertEqual(minesweeper_game.check_won(minesweeper_game.player_map), False)

    def test_check_won_2(self):
        minesweeper_game = MinesweeperGame(3, 1)
        minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        minesweeper_game.player_map = [['-', '-', '-'], ['-', 1, '-'], ['-', '-', '-']]
        self.assertEqual(minesweeper_game.check_won(minesweeper_game.player_map), False)

    def test_check_won_3(self):
        minesweeper_game = MinesweeperGame(3, 0)
        minesweeper_game.minesweeper_map = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        minesweeper_game.player_map = [['-', '-', '-'], ['-', 1, '-'], ['-', '-', '-']]
        self.assertEqual(minesweeper_game.check_won(minesweeper_game.player_map), False)

import unittest

class AgentTest_check_won(unittest.TestCase):
    def test_check_won_1(self):
        minesweeper_game = MinesweeperGame(3, 1)
        minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        minesweeper_game.player_map = [['-', 1, 0], [1, 1, 0], [0, 0, 0]]
        self.assertEqual(minesweeper_game.check_won(minesweeper_game.player_map), True)

    def test_check_won_2(self):
        minesweeper_game = MinesweeperGame(3, 2)
        minesweeper_game.minesweeper_map = [['X', 'X', 1], [2, 2, 1], [0, 0, 0]]
        minesweeper_game.player_map = [['-', '-', 1], [2, 2, 1], [0, 0, 0]]
        self.assertEqual(minesweeper_game.check_won(minesweeper_game.player_map), True)

class MinesweeperGameTestSweep(unittest.TestCase):
    def test_sweep(self):
        minesweeper_game = MinesweeperGame(3, 1)
        minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        minesweeper_game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.assertEqual(minesweeper_game.sweep(1,1), [['-', '-', '-'], ['-', 1, '-'], ['-', '-', '-']])
        self.assertEqual(minesweeper_game.score, 1)

    def test_sweep_2(self):
        minesweeper_game = MinesweeperGame(3, 1)
        minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        minesweeper_game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.assertEqual(minesweeper_game.sweep(0,0), False)
        self.assertEqual(minesweeper_game.score, 0)

    def test_sweep_3(self):
        minesweeper_game = MinesweeperGame(3, 1)
        minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        minesweeper_game.player_map = [['-', '-', '0'], ['1', '1', '0'], ['0', '0', '0']]
        self.assertEqual(minesweeper_game.sweep(0,1), True)
        self.assertEqual(minesweeper_game.score, 1)

import unittest

class AgentTest_sweep(unittest.TestCase):
    def test_sweep_1(self):
        minesweeper_game = MinesweeperGame(3, 1)
        minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        minesweeper_game.player_map = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.assertEqual(minesweeper_game.sweep(1, 0),
                         [['-', '-', '-'], [1, '-', '-'], ['-', '-', '-']])

    def test_sweep_2(self):
        minesweeper_game = MinesweeperGame(3, 1)
        minesweeper_game.minesweeper_map = [['X', 1, 0], [1, 1, 0], [0, 0, 0]]
        minesweeper_game.player_map = [['-', 1, 0], [1, 1, 0], [0, 0, '-']]
        self.assertEqual(minesweeper_game.sweep(2, 2), True)