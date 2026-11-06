class PushBoxGame:
    """
    This class implements a functionality of a sokoban game, where the player needs to move boxes to designated targets in order to win.
    """

    def __init__(self, map):
        """
        Initialize the push box game with the map and various attributes.
        :param map: list[str], the map of the push box game, represented as a list of strings. 
            Each character on the map represents a different element, including the following:
            - '#' represents a wall that neither the player nor the box can pass through;
            - 'O' represents the initial position of the player;
            - 'G' represents the target position;
            - 'X' represents the initial position of the box.
        >>> map = ["#####", "#O  #", "# X #", "#  G#", "#####"]   
        >>> game = PushBoxGame(map)                
        """
        self.map = map
        self.player_row = 0
        self.player_col = 0
        self.targets = []
        self.boxes = []
        self.target_count = 0
        self.is_game_over = False
        self.init_game()

    def init_game(self):
        """
        Initialize the game by setting the positions of the player, targets, and boxes based on the map.
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
        >>> game.targets
        [(3, 3)]
        >>> game.boxes
        [(2, 2)]
        >>> game.player_row
        1
        >>> game.player_col
        1
        """
        self.player_row = 0
        self.player_col = 0
        self.targets = []
        self.boxes = []
        self.is_game_over = False

        for r, row in enumerate(self.map):
            for c, ch in enumerate(row):
                if ch == 'O':
                    self.player_row, self.player_col = r, c
                elif ch == 'G':
                    self.targets.append((r, c))
                elif ch == 'X':
                    self.boxes.append((r, c))

        self.target_count = len(self.targets)

    def _is_wall(self, r, c):
        if r < 0 or r >= len(self.map):
            return True
        row = self.map[r]
        if c < 0 or c >= len(row):
            return True
        return row[c] == '#'

    def print_map(self):
        """
        Print the current state of the map.
        """
        boxes = set(self.boxes)
        targets = set(self.targets)
        for r, row in enumerate(self.map):
            cells = []
            for c, ch in enumerate(row):
                if ch == '#':
                    cells.append('#')
                elif r == self.player_row and c == self.player_col:
                    cells.append('O')
                elif (r, c) in boxes:
                    cells.append('X')
                elif (r, c) in targets:
                    cells.append('G')
                else:
                    cells.append(' ')
            print(' '.join(cells))

    def check_win(self):
        """
        Check if the game is won. The game is won when all the boxes are placed on target positions.
        And update the value of self.is_game_over.
        :return self.is_game_over: True if all the boxes are placed on target positions, or False otherwise.
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
        >>> game.check_win()
        """
        targets = set(self.targets)
        self.is_game_over = all(box in targets for box in self.boxes)
        return self.is_game_over

    def move(self, direction):
        """
        Move the player based on the specified direction and check if the game is won.
        :param direction: str, the direction of the player's movement. 
            It can be 'w', 's', 'a', or 'd' representing up, down, left, or right respectively.

        :return: True if the game is won, False otherwise.
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"])       
        >>> game.print_map()
        # # # # # 
        # O     #
        #   X   #
        #     G #
        # # # # #
        >>> game.move('d')
        False
        >>> game.move('s')   
        False
        >>> game.move('a')   
        False
        >>> game.move('s') 
        False
        >>> game.move('d') 
        True
        """
        deltas = {'w': (-1, 0), 's': (1, 0), 'a': (0, -1), 'd': (0, 1)}
        if direction not in deltas:
            return self.check_win()

        dr, dc = deltas[direction]
        nr, nc = self.player_row + dr, self.player_col + dc

        if self._is_wall(nr, nc):
            return self.check_win()

        if (nr, nc) in self.boxes:
            br, bc = nr + dr, nc + dc
            if self._is_wall(br, bc) or (br, bc) in self.boxes:
                return self.check_win()
            idx = self.boxes.index((nr, nc))
            self.boxes[idx] = (br, bc)

        self.player_row, self.player_col = nr, nc
        return self.check_win()