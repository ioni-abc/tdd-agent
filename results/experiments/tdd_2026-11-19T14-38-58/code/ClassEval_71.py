import unittest


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
        self.targets = []
        self.boxes = []
        for row, line in enumerate(self.map):
            for col, ch in enumerate(line):
                if ch == 'O':
                    self.player_row = row
                    self.player_col = col
                elif ch == 'G':
                    self.targets.append((row, col))
                elif ch == 'X':
                    self.boxes.append((row, col))
        self.target_count = len(self.targets)

    def _is_wall(self, row, col):
        if row < 0 or row >= len(self.map):
            return True
        line = self.map[row]
        if col < 0 or col >= len(line):
            return True
        return line[col] == '#'

    def check_win(self):
        """
        Check if the game is won. The game is won when all the boxes are placed on target positions.
        And update the value of self.is_game_over.
        :return self.is_game_over: True if all the boxes are placed on target positions, or False otherwise.
        >>> game = PushBoxGame(["#####", "#O  #", "# X #", "#  G#", "#####"]) 
        >>> game.check_win()
        """
        self.is_game_over = all(box in self.targets for box in self.boxes)
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
        new_row = self.player_row + dr
        new_col = self.player_col + dc

        if self._is_wall(new_row, new_col):
            return self.check_win()

        if (new_row, new_col) in self.boxes:
            box_row = new_row + dr
            box_col = new_col + dc
            if self._is_wall(box_row, box_col) or (box_row, box_col) in self.boxes:
                return self.check_win()
            idx = self.boxes.index((new_row, new_col))
            self.boxes[idx] = (box_row, box_col)

        self.player_row = new_row
        self.player_col = new_col
        return self.check_win()