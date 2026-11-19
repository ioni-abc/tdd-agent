import random


class MahjongConnect:
    """
    MahjongConnect is a class representing a game board for Mahjong Connect with features like creating the board, checking valid moves, finding paths, removing icons, and checking if the game is over.
    """

    EMPTY = ' '
    DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

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
        n = len(self.ICONS)
        return [[self.ICONS[c % n] for c in range(cols)] for _ in range(rows)]

    def _in_bounds(self, r, c):
        return 0 <= r < len(self.board) and 0 <= c < len(self.board[0])

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
        r1, c1 = pos1
        r2, c2 = pos2
        if not self._in_bounds(r1, c1) or not self._in_bounds(r2, c2):
            return False
        if (r1, c1) == (r2, c2):
            return False
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
        r1, c1 = pos1
        r2, c2 = pos2
        end = (r2, c2)
        # State: at cell (r, c), intending to move in direction d, with t turns used so far.
        stack = [(r1, c1, d, 0) for d in self.DIRECTIONS]
        visited = set()
        while stack:
            r, c, d, t = stack.pop()
            state = (r, c, d, t)
            if state in visited:
                continue
            visited.add(state)
            nr, nc = r + d[0], c + d[1]
            if not self._in_bounds(nr, nc):
                continue
            if (nr, nc) == end:
                return True
            if self.board[nr][nc] != self.EMPTY:
                continue
            # Continue straight
            stack.append((nr, nc, d, t))
            # Turn perpendicular, costing one turn
            if t + 1 <= 2:
                for nd in self.DIRECTIONS:
                    if nd[0] * d[0] + nd[1] * d[1] == 0:
                        stack.append((nr, nc, nd, t + 1))
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
        for row in self.board:
            for cell in row:
                if cell != self.EMPTY:
                    return False
        return True