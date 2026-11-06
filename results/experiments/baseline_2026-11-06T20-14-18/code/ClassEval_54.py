import random
from collections import deque


class MahjongConnect:
    """
    MahjongConnect is a class representing a game board for Mahjong Connect with features like creating the board, checking valid moves, finding paths, removing icons, and checking if the game is over.
    """

    EMPTY = ' '
    # Directions as (row delta, column delta): up, right, down, left
    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

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
        rows, cols = self.BOARD_SIZE[0], self.BOARD_SIZE[1]
        num_icons = len(self.ICONS)
        return [[self.ICONS[c % num_icons] for c in range(cols)]
                for _ in range(rows)]

    def _in_bounds(self, pos):
        rows, cols = self.BOARD_SIZE[0], self.BOARD_SIZE[1]
        r, c = pos
        return 0 <= r < rows and 0 <= c < cols

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
        if not (self._in_bounds(pos1) and self._in_bounds(pos2)):
            return False
        if tuple(pos1) == tuple(pos2):
            return False
        r1, c1 = pos1
        r2, c2 = pos2
        icon1 = self.board[r1][c1]
        icon2 = self.board[r2][c2]
        if icon1 == self.EMPTY or icon2 == self.EMPTY:
            return False
        if icon1 != icon2:
            return False
        return self.has_path(pos1, pos2)

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
        if not (self._in_bounds(pos1) and self._in_bounds(pos2)):
            return False
        pos1 = tuple(pos1)
        pos2 = tuple(pos2)
        if pos1 == pos2:
            return False

        # BFS over states (row, col, direction, turns); a path may turn at most twice.
        start = (pos1[0], pos1[1], None, 0)
        queue = deque([start])
        best_turns = {}

        while queue:
            r, c, d, t = queue.popleft()
            for nd, (dr, dc) in enumerate(self.DIRECTIONS):
                if d is not None and nd == (d + 2) % 4:
                    continue  # reversing direction is never useful
                nt = t + (1 if d is not None and nd != d else 0)
                if nt > 2:
                    continue
                nr, nc = r + dr, c + dc
                if not (0 <= nr < self.BOARD_SIZE[0] and 0 <= nc < self.BOARD_SIZE[1]):
                    continue
                if (nr, nc) == pos2:
                    return True
                if self.board[nr][nc] != self.EMPTY:
                    continue
                key = (nr, nc, nd)
                if key in best_turns and best_turns[key] <= nt:
                    continue
                best_turns[key] = nt
                queue.append((nr, nc, nd, nt))
        return False

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
        r1, c1 = pos1
        r2, c2 = pos2
        self.board[r1][c1] = self.EMPTY
        self.board[r2][c2] = self.EMPTY

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
        return all(cell == self.EMPTY for row in self.board for cell in row)