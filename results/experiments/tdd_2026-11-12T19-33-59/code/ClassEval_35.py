import copy


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
        for i, row in enumerate(state):
            for j, value in enumerate(row):
                if value == 0:
                    return (i, j)
        return None

    def move(self, state, direction):
        """
        Find the blank block, then makes the board moves forward the given direction.
        :param state: a 3*3 size list of Integer, stores the state before moving.
        :param direction: str, only has 4 direction 'up', 'down', 'left', 'right'
        :return new_state: a 3*3 size list of Integer, stores the state after moving.
        >>> eightPuzzle.move([[2, 3, 4], [5, 8, 1], [6, 0, 7]], 'left')
        [[2, 3, 4], [5, 8, 1], [0, 6, 7]]
        """
        new_state = copy.deepcopy(state)
        blank = self.find_blank(new_state)
        if blank is None:
            return new_state

        i, j = blank
        offsets = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1),
        }
        if direction not in offsets:
            return new_state

        di, dj = offsets[direction]
        ni, nj = i + di, j + dj
        if 0 <= ni < len(new_state) and 0 <= nj < len(new_state[ni]):
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
        return new_state

    def get_possible_moves(self, state):
        """
        According the current state, find all the possible moving directions. Only has 4 direction 'up', 'down', 'left', 'right'.
        :param state: a 3*3 size list of Integer, stores the current state.
        :return moves: a list of str, store all the possible moving directions according to the current state.
        >>> eightPuzzle.get_possible_moves([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        ['up', 'left', 'right']
        """
        blank = self.find_blank(state)
        if blank is None:
            return []

        i, j = blank
        offsets = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1),
        }
        moves = []
        for direction, (di, dj) in offsets.items():
            ni, nj = i + di, j + dj
            if 0 <= ni < len(state) and 0 <= nj < len(state[ni]):
                moves.append(direction)
        return moves

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
        if self.initial_state is None:
            return None

        start = copy.deepcopy(self.initial_state)
        if start == self.goal_state:
            return []

        def key(state):
            return tuple(tuple(row) for row in state)

        open_list = [(start, [])]
        visited = {key(start)}

        while open_list:
            state, path = open_list.pop(0)
            for direction in self.get_possible_moves(state):
                new_state = self.move(state, direction)
                new_key = key(new_state)
                if new_key in visited:
                    continue
                new_path = path + [direction]
                if new_state == self.goal_state:
                    return new_path
                visited.add(new_key)
                open_list.append((new_state, new_path))

        return None